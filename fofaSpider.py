# encoding=utf8
import fofa
import argparse
import multiprocessing
import time 
#参数
def Args():
    parse = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,add_help=False,description='''
    *===================================*
    |    Please set the parameters!     |
    |    Author:ivonne                  |
    |    Version:1.0                    |
    |    Time:2018/01/17                |
    *===================================*
    ''')
    parse.add_argument('-m','--mail',help='Please set mail')
    parse.add_argument('-k','--key',help="Please set key")
    parse.add_argument('-r','--rule',help="Please set rule")
    parse.add_argument('-f','--file',default='res.txt',help='Please set file')
    parse.add_argument('-s','--start',help='Please set start_page')
    parse.add_argument('-e','--end',help='Please set end_page')
    parse.add_argument('-t','--thread',default=1,help='Please set thread number',type=int)
    args = parse.parse_args()
    if args.mail is None and args.key is None and args.rule is None and args.file is None and args.start is None and args.end is None:
    	
        print parse.print_help()
        exit()
    else :
        return args
#fofa启动函数
def fofaStart(mail,key,rule,file,start,end):
	client = fofa.Client(mail,key)                                 
	query_str = rule
	try:
		with open(file,'a') as fi:
			for page in range(int(start),int(end)): 
				print '第%d页'%page                                         
				data = client.get_data(query_str,page=page,fields="ip,city")  
				for ip,city in data["results"]:
					fi.write('[%s]: %s\n'%(ip,city))  
	except Exception as e:
		pass	

if __name__ == "__main__":
	args = Args()
	pool = multiprocessing.Pool(processes=int(args.thread))
	start = time.clock()
	pool.apply_async(fofaStart,(args.mail,args.key,args.rule,args.file,args.start,args.end,))
	pool.close()
	pool.join()
	end = time.clock()
	print 'Running time: %f Seconds'%(end-start)


                     
