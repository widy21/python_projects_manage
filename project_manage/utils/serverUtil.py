#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import os
import paramiko

__author__ = 'Monkey.D.xiao'

class ServerUtil(object):

    def __init__(self):
        pass

    def exec_command_pwd(self,hostname,port,username,password,commond):
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(hostname,port,username,password)
        print 'connect success...'
        stdin,stdout,stderror = con.exec_command(commond)
        result = stdout.read(),stderror.read()
        con.close()
        return result

    def exec_command_key(self,hostname,port,username,password,key_file,commond):
        con = paramiko.SSHClient()
        con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        con.connect(hostname,port,username,password,key_filename=key_file,timeout=50)
        stdin,stdout,stderror = con.exec_command(commond)
        result = stdout.read(),stderror.read()
        con.close()
        return result

    def upload_file(self,hostname,port,username,password,local_dir,remote_dir):
        try:
            t = paramiko.Transport((hostname, port))
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            os.chdir(local_dir)
            files=os.listdir(local_dir)
            for f in files:
                print'Beginning to upload file %s to %s' % (os.path.join(local_dir,f),remote_dir+'/'+f)
                #上传
                sftp.put(os.path.join(local_dir,f),remote_dir+'/'+f)
            t.close();
        except Exception, e:
            import traceback
            traceback.print_exc()
        try:
            t.close()
        except:
            pass

    def upload_single_file(self,hostname,port,username,password,file_path,remote_dir,file_name):
        try:
            t = paramiko.Transport((hostname, port))
            t.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            print 'Beginning to upload file %s to %s' % (file_path,remote_dir+'/'+file_name)
            #上传
            sftp.put(file_path,remote_dir+'/'+file_name)
            t.close();
        except Exception, e:
            import traceback
            traceback.print_exc()
        try:
            t.close()
        except:
            pass


    def download_file(self,hostname,port,username,password,local_dir,remote_dir,download_file_list):
        try:
            t = paramiko.Transport((hostname, port))
            t.connect(username=username, password=password)
            sftp =paramiko.SFTPClient.from_transport(t)

            files=sftp.listdir(remote_dir)
            for f in files:
                if self.containsFile(str(f),download_file_list):
                    # print f
                    print'Beginning to download file from %s to %s' % (remote_dir+'/'+f,os.path.join(local_dir,f))
                    sftp.get(remote_dir+'/'+f,os.path.join(local_dir,f))
            t.close();
        except Exception, e:
            import traceback
            traceback.print_exc()
        try:
            t.close()
        except:
            pass


    def download_file_with_key(self,hostname,port,username,password,key_file,local_dir,remote_dir,download_file_list):
        try:
            #t = paramiko.Transport((hostname, port))
            # t.connect(username=username, password=password)
            #sftp =paramiko.SFTPClient.from_transport(t)

            con = paramiko.SSHClient()
            con.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            con.connect(hostname,port,username,password,key_filename=key_file,timeout=50)
            t = con.get_transport()
            sftp=paramiko.SFTPClient.from_transport(t)

            files=sftp.listdir(remote_dir)
            for f in files:
                if self.containsFile(str(f),download_file_list):
                    # print f
                    print'Beginning to download file from %s to %s' % (remote_dir+'/'+f,os.path.join(local_dir,f))
                    sftp.get(remote_dir+'/'+f,os.path.join(local_dir,f))
            t.close();
        except Exception, e:
            import traceback
            traceback.print_exc()
        try:
            t.close()
        except:
            pass

    def containsFile(self,f, download_file_list_str):
        for file in download_file_list_str:
            if f == file:
                return True
        return False

    def inred(self,s):
        return"%s[33;2m%s%s[0m"%(chr(27), s, chr(27))

    def query_content(self,localdir,content):

        res_list = []
        files = os.listdir(localdir)
        for f in files:
            path = os.path.join(localdir, f)
            res_list.append(self.inred(path+"--> "))
            f1 = open(path)
            for line in f1:
                # print line
                if content in line:
                    res_list.append("  "+line.replace(content,self.inred(content)))

        for i in res_list:
            print i