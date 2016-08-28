#!/usr/bin/python
# -*- coding: utf-8 -*-

# this code mount E01 to ewf1, and all ntfs partitions in the source ewf file
# use: python ewf_part_mount.py 'path.E01'

import subprocess, sys
from time import sleep

def ewf_mount(filename):    
    path_ewf = input('destination mount folder for ewf: ').strip()    
    subprocess.Popen(['sudo', 'ewfmount', filename, path_ewf], stdin = subprocess.PIPE).communicate()
    subprocess.Popen(['sudo', 'mmls', path_ewf + '/ewf1'], stdin = subprocess.PIPE)
    part_mount(path_ewf)

def part_mount(path_ewf):
    part_numb = 0
    mmls_cmd = subprocess.Popen(['sudo', 'mmls', path_ewf + '/ewf1'], stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    for i in range(0, 20):
        line = mmls_cmd.stdout.readline().decode('utf-8', 'ignore').strip().split()
        if len(line) > 6 and line[5] == 'NTFS':
            dest_mount_point = '/mnt/part' + str(part_numb)
            subprocess.Popen(['sudo', 'mkdir', dest_mount_point], stdin = subprocess.PIPE)
            offset = 'ro,loop,show_sys_files,streams_interface=windows,offset='+ str(int(line[2])*512)
            subprocess.Popen(['sudo', 'mount', '-t', 'ntfs-3g', '-o', offset, path_ewf + '/ewf1', dest_mount_point], stdin = subprocess.PIPE)
            part_numb += 1
        i += 1

def ewf_umount():    
    subprocess.Popen(['sudo', 'umount', '/mnt/part0'], stdin = subprocess.PIPE).communicate()
    subprocess.Popen(['sudo', 'umount', '/mnt/part1'], stdin = subprocess.PIPE)
    subprocess.Popen(['sudo', 'umount', '/mnt/part2'], stdin = subprocess.PIPE)
    sleep(1)
    subprocess.Popen(['sudo', 'umount', '/mnt/efi'], stdin = subprocess.PIPE)
    
#ewf_mount(sys.argv[1])
#python -c 'from ewf_part_mount import *; ewf_mount("/mnt/Ta/Le/nav/fekiszeverkklac/fekiszerverkklac.E01")'
#python -c 'from ewf_part_mount import *; ewf_umount()'
