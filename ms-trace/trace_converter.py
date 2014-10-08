import argparse
import sys

DISK_NAME = ""

def write_trace_mgmt_format(h_tf):
    h_tf.write("fio version 2 iolog\n")	
    h_tf.write(DISK_NAME+ " "+"add"+"\n")
    h_tf.write(DISK_NAME+ " "+"open"+ "\n")

def write_io_action_format(in_tf,out_tf):
    while True:
        line=in_tf.readline()
        if not line:
             break
        line_lst = line.split(",")
        #print line_lst
        out_type= line_lst[3].lower()
        out_offset = line_lst[4]
        out_size = line_lst[5] 
        #print "out is " + out_type + out_offset+ out_size
        w_line =DISK_NAME + " " + out_type  + " "+out_offset+" "+ out_size + "\n"
        out_tf.write(w_line)

def main(argv):
    #print "tracefile is " + argv[0]
    global DISK_NAME
    parser = argparse.ArgumentParser(description='Convert microsoft research traces into fio compatible traces to be run on Shingled disk.\n')
    parser.add_argument('-if', action="store",help="input MS Tracefile name",dest="in_trace_file",required=True,type=str)
    parser.add_argument('-d',action="store",help="disk name",dest="disk_name",required=True,type=str)
    parser.add_argument('-of',action="store",help="Output fio filename to be generated",dest="out_trace_file",required=True,type=str)
    results = parser.parse_args()
    IN_TRACEFILE = results.in_trace_file
    DISK_NAME = results.disk_name
    OUT_TRACEFILE = results.out_trace_file 
    print "input ms tracefile is : " + IN_TRACEFILE 
    print "output fio  tracefile is : " + OUT_TRACEFILE
    print "disk name is  : " + DISK_NAME
    out_tf = open(OUT_TRACEFILE,"w") 
    in_tf = open(IN_TRACEFILE,"r")  
    write_trace_mgmt_format(out_tf)
    write_io_action_format(in_tf,out_tf)
    out_tf.write(DISK_NAME + " "+"close")
    out_tf.close()
          
    in_tf.close()
          
#f.close()
if __name__ == "__main__":
    main(sys.argv)
