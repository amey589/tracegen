import random as random1
import sys
import argparse
SEG_SIZE=16777216
PAGE_SIZE=4096
DISK_NAME="/dev/sdb"
NUM_16MB_SEG=178813
WRITE_PERCENT=25 #Default WRITE_PERCENT
BURST_SIZE=10
def reset1(percent,total):
   no =  random1.randrange(total) 
   print "percent: " + str(percent) + "total :" + str(total) + "rand :"+str(no) 
   if no <  percent:
       return True
   else:
       return False

def count_true_in_list(lst):
    index = 0
    for item in lst:
        if item==True:
             index = index + 1
    return index 
   #def sample():
#    lst = [reset1(WRITE_PERCENT,PAGE_SIZE) for x in range(PAGE_SIZE)]
#    count_true_in_list(lst)

def generate_complex_trace_lst():
    lst = []
    p = False
    
    #print "sample results are",
    #sample()
    #print "---------------"
    index = 0
    while(len(lst) < PAGE_SIZE):
        new_write_percent = int((WRITE_PERCENT * (PAGE_SIZE-index))/100)
        if p is True:
            for i in range(BURST_SIZE):
                #reset1(new_write_percent,(PAGE_SIZE-index))
                lst.append(True)
            print "Burst at " + str(index)
            #random1.seed(seedvalue)
        elif p is False:
           #print p
           lst.append(False)
        #print "index is" + str(index),
        p = reset1(new_write_percent,(PAGE_SIZE-index))
        index = index + 1
    true_count = count_true_in_list(lst)
    #print a
    print("\n")
    print "No of blocks will be written : {0}\npage size : {1} \
       \nwrite percent : {2} \nburst size : {3}".format(true_count,PAGE_SIZE,WRITE_PERCENT,BURST_SIZE)
    
    return lst

def reset(percent):   
       return random.randrange(PAGE_SIZE) > percent

def calculate_percent(wr_inv):
    a = (wr_inv * PAGE_SIZE)/100
    #print a 
    return a

def write_trace_mgmt_format(h_tf):
    h_tf.write("fio version 2 iolog\n")	
    h_tf.write(DISK_NAME+ " "+"add"+"\n")
    h_tf.write(DISK_NAME+ " "+"open"+ "\n")

def write_io_action_format(h_tf):
    index = 0
    print "WRITE PERCENT is " + str(WRITE_PERCENT)
    percent = calculate_percent(100-WRITE_PERCENT)
    #page_list = [reset(percent) for x in range(0,PAGE_SIZE)]
    page_list = generate_complex_trace_lst()
    r = random1.randint(0,NUM_16MB_SEG)
    segment_start_addr=SEG_SIZE * r
    print "random 16 MB segment starts at " + str(segment_start_addr)
    #f = open(DISK_NAME,"w")
    #f.seek(segment_start_addr,0)
    page_start_addr=0
    #WRITE_DATA = "".join(["K" for x in range(0,PAGE_SIZE)])
    #print page_list
    for page_number in range(0,PAGE_SIZE-1):
        if page_list[page_number] == True:
            page_start_addr = segment_start_addr + page_number*PAGE_SIZE
            h_tf.write(DISK_NAME+ " " + "write"+ " "+ str(page_start_addr) + " " + str(PAGE_SIZE)+ "\n")
            #f.seek(page_start_addr,1)
            #f.write(WRITE_DATA)

def main(argv):
    #print "tracefile is " + argv[0]
    global WRITE_PERCENT
    seed_value=1
    random1.seed(seed_value)
    parser = argparse.ArgumentParser(description='generate traces for replaying on disks.')
    parser.add_argument('-f', action="store",help="Tracefile name",dest="trace_file",required=True,type=str)
    parser.add_argument('-w',action="store",help="write percentage:default is 25",default=25,dest="write_percent",type=int)
    results = parser.parse_args()
    TRACEFILE = results.trace_file
    WRITE_PERCENT = results.write_percent
    h_tf = open(TRACEFILE,"w")
    write_trace_mgmt_format(h_tf)
    #write_io_action_format(h_tf)
    for i in range(1):
         write_io_action_format(h_tf) 
    h_tf.write(DISK_NAME + " "+"close")
    h_tf.close()
          
#f.close()
if __name__ == "__main__":
    main(sys.argv)
