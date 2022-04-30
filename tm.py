import shutil
import pathlib
import zipfile
import os

res_root_dir = "aaa"       #圧縮するリソースフォルダ名
beh_root_dir = "bbb"       #圧縮するビヘイビアフォルダ名


# この二つは異なる名前にしてください
pack_res_name = "res"     #リソースを圧縮した名前  〇〇.mcpackの〇〇
pack_beh_name = "beh"     #ビヘイビアを圧縮した名前  〇〇.mcpackの〇〇

add_name     = "sword"     #〇〇.mcaddonの〇〇部分

#拡張子変える関数
def change_file(file_name, to_suf):
    t = pathlib.PurePath(file_name).stem
    to_name = t + to_suf
    shutil.move(file_name, to_name)

shutil.make_archive(pack_res_name, format="zip", root_dir=res_root_dir)
shutil.make_archive(pack_beh_name, format="zip", root_dir=beh_root_dir)

change_file(pack_res_name+".zip", ".mcpack")
change_file(pack_beh_name+".zip", ".mcpack")

with zipfile.ZipFile("./"+add_name+".zip", "w", compression=zipfile.ZIP_DEFLATED) as z:
    z.write("./"+pack_res_name+".mcpack")
    z.write("./"+pack_beh_name+".mcpack")
    

change_file(add_name+".zip", ".mcaddon")


os.remove(pack_res_name+".mcpack")
os.remove(pack_beh_name+".mcpack")