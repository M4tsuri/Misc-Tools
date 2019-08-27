#!/usr/bin/env bash
## 实现usage [-h help][--decode decode] etc
## 1.a little decode programe supportng base64, rot13;
## --decode -f file -s string
## 2.a tool for merging files;
## --merge -p path
## 3.a tool for removing deFlags form fake encoded zip;
## --fakezip -f file
## 4.a tool for repairing broken png image;
## --repng -f file
ARGS=$(getopt f:s::p: -- "$@")
eval set -- "$ARGS"
ori_path=$(pwd)
shift # feature（困惑）：为什么去掉这句就错了

case "$1" in
--decode)
  case "$2" in
  -f)
    python /Volumes/Data/CTF/TOOLS/decode.py f "$ori_path"/"$3";;
  -s)
    python /Volumes/Data/CTF/TOOLS/decode.py s "$3" "$4";;
  *)
    echo "ARGS ERROR";;
  esac;;
## -f file -s string
--merge)
  case "$2" in
  -p)
    ctf_mv.sh "$ori_path"/"$3";;
  *)
    echo "ARGS ERROR";;
  esac;;
--fakezip)
  case "$2" in
  -f)
    python /Volumes/Data/CTF/TOOLS/remove_deflags.py "$ori_path"/"$3";;
  *)
    echo "ARGS ERROR";;
  esac;;
--repng)
  case "$2" in
  -f)
    python2 "$CTFTOOLS"/PCRT/PCRT.py -i "$ori_path"/"$3";;
  *)
    echo "ARGS ERROR";;
  esac;;
*)
  echo Error Input!;;
esac

