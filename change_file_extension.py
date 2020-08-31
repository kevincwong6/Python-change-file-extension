'''A Python script to change all video file extension, '''
'''from provided directory and all it's subdirtories   '''
#!/usr/bin/env python
import os
import sys

def does_dir_exist(dir_name):
    '''Check directory exist or not'''
    if not os.path.isdir(dir_name):
        err_msg = 'Error: Directory, ' + dir_name + ', does not exist'
        print(err_msg)
        return False

    return True

def change_file_extension(orig_file, orig_ext, new_ext, cnt=None):
    '''Check video file during'''
    cnt_str = ''
    if cnt:
        cnt_str = str(cnt) + ') '
    print(cnt_str + 'Processing ' + orig_file)

    try:
        new_file = orig_file.rsplit(orig_ext, 1)
        os.rename(orig_file, new_file[0]+new_ext)
    except:
        ex = sys.exc_info()[0]
        err_msg = "Error: failed to process %s (%s)." % (orig_file, ex)
        print(err_msg)
        sys.exit(1)   
    cnt += 1     

def check_all_files(path, orig_ext, new_ext):
    cnt = 1    
    for root, _, files in os.walk(path):
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith(orig_ext):
               change_file_extension(filename, orig_ext, new_ext, cnt)
               cnt += 1

def run(path):
    if does_dir_exist(path):
        check_all_files(path, '.txt', '.kviw')

path = './'     
if len(sys.argv) > 1:
    path = sys.argv[1]
    
run(path)
sys.exit(0)
