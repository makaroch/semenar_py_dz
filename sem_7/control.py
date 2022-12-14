import  viem
import inpyt
import outpyt
import transfor

def main():
    flag = viem.inpyt_in_or_out()
    if flag == '1':
        string = viem.inpyt()
        str_list = transfor.transfor(string)
        print(str_list)
        inpyt.import_data(str_list)
    else:
        string = viem.out()
        numers_list = outpyt.export_data(string)
        viem.print_search(numers_list)

