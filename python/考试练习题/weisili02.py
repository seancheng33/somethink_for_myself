'''
@Author       : sean cheng
@Email        : aya234@163.com
@CreateTime   : 2018/8/31
@Program      : 统计《寻梦》《命运》两书的前100个字相同字符
'''
import jieba


def readfile(filename):
    with open(filename+'-汉字统计.txt','r',encoding='utf-8') as infile:
        words = infile.read().split(',')
        newls = []
        for word in words:
            newls.append(word.split(':')[0])
        
    return newls
    
def main():
    ls1 = readfile('寻梦')
    ls2 = readfile('命运')
    ls3 = []
    for i in ls1:
        for j in ls2:
            if i == j:
                ls3.append(i)
    with open('相同字符.txt','w',encoding='utf-8') as outfile:
        outfile.write(','.join(ls3))
    
    
if __name__ == '__main__':
    main()
