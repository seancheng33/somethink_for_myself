'''
@Author : sean cheng
@Email  : aya234@163.com
@Create_Time   : 18/6/1 
@Program  : jieba分词基础训练题
'''
import jieba
import jieba.posseg
import jieba.analyse

data = u'孙悟空被压在五行山下五百年，直到唐僧揭开封印救他出来，才终于能一展拳脚。取经路上，唐僧每隔几天，就要乱跑出去，每次出去，都惹些祸事。孙悟空不止一次地跑去救他，降妖除魔。又一次，孙悟空将白骨精毙于棍下，转身离开。待悟空走远，白骨精重新聚成人形。“真是不好意思呀。”唐僧不断地拜谢，“没想到这一路遇到的妖精都这么善良，之后到了佛祖那里，我一定会如实禀报你们的善行。”“都是些举手之劳，能做些善事自然是好的。我不求回报，长老真的不要费心了！”白骨精急忙摆手，然后又小心翼翼地问道，“只是不知道您耗费这么大力气，是为了什么。”“听说那猴子以前是齐天大圣，要强得很。可他压在山下那么多年，法力又怎么可能不退步，若是被他知道真相，大概会很伤心吧。”唐僧道，“只好拜托你们陪我演这出戏，除了一开始遇到的那几只妖精，居然都愿意帮我。”孙悟空远远望着这一幕，扛着棍子，一个筋斗远去。“这傻和尚。”孙悟空笑着摇头，敲响了面前的山门。“你谁啊？”妖精开门，皱起眉头。“你孙爷爷。”孙悟空棒子一甩，顶住妖精额头，“过会儿有个小和尚要来，你演出戏，让他以为世界充满善意。”“不干就打死你。”'

jieba.load_userdict('userdict.txt')
# wordlist = jieba.cut(data)
# print('|'.join(wordlist))
#
#
# wordlist = jieba.posseg.cut(data)
# for item in wordlist:
#     print('词：'+item.word, '词性：'+item.flag)

tags = jieba.analyse.extract_tags(data, topK=5)
print('|'.join(tags))