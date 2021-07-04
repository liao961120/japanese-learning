#%% 
import re

DICT = './bin/hj_linux_amd64'
pat_word = re.compile(r'^\S+ (\[[^][ ]+\]){1,2}')
pat_url = re.compile(r'http\S+$')

def match_all(output):
    heads = []
    append_next = False
    for i, line in enumerate(output.split('\n')):
        if i == 0:
            heads.append(line)
            continue
        if line.strip() == '':
            append_next = True
            continue
        if append_next:
            heads.append(line.strip())
            append_next = False

    matched = []
    for head in heads:
        word = pat_word.search(head)
        url = pat_url.search(head)

        if word is None or url is None:
            print(f"Failed to match {head}")
            print(head)
        else:
            matched.append([word[0], url[0]])
    
    return matched
        
s = '''令 [れい][rei]① https://tts.hjapi.com/jp/2EBB461B55B703F8
simple explain:
 【名词】
   1.命令;法令;长官
More Detail:
 word attribute: 接頭
  1.相手の親族に対する尊敬の意を表す。令。
    1)令兄。
      令兄。
    2)令嬢。
      令爱。令嫒。
    3)令夫人。
      尊夫人。夫人。太太。
    4)令妹。
      令妹。
    5)令姉。
      令姐。
    6)令婿。
      令婿。
    7)令息。
      令郎。
    8)令弟。
      令弟。

礼 [れい][rei]① http://d1.g.hjfile.cn/voice/jpsound/C1035.mp3
simple explain:
 【名词】
   1.礼,礼貌；礼法；礼节；礼仪。〔礼儀。〕
   2.敬礼,行礼；鞠躬。〔敬礼。〕
   3.道谢,致谢；谢词；感谢,谢。〔謝意。〕
More Detail:
 word attribute: 名词
  1.人のふみ行うべき道。社会生活上の定まった形式。礼节。礼貌。礼。
    1)礼を尽す。
      尽礼节。
    2)礼を失する。
      失礼。
    3)礼をわきまえない。
      不懂礼节。
  2.中国上代の，礼を書きしるした書物。礼记。
  3.敬意をもってきまりに従う。うやまっておじぎをする。低頭などして敬意を表す。敬礼。鞠躬。
    1)お墓に礼をする。
      向墓敬礼。
    2)目礼。
      注目礼。
  4.謝意をあらわす。そのための金品。道谢。致谢。答谢。酬谢。
    1)お礼を言う。
      道谢。
    2)礼を送る。
      赠送礼品。

レイ [れい][rei]① https://tts.hjapi.com/jp/F4EF9F771C8BC922
simple explain:
 【名词】
   1.【夏威夷】lei ;花环。夏威夷花链。夏威夷人为欢迎客人而戴在客人颈上的、用木槿属植物等制作的花环。（首にかける花輪。もとハワイ諸島民が儀礼などに用いた。現在は旅行者の歓迎などに使用する。）
More Detail:
 word attribute: 名词
  1.ハワイで歓迎・歓送の気持ちを表すために，相手の首にかける花輪。（夏威夷人给来访者带的用以表示欢迎或欢送的）花环。

例 [れい][rei]① https://tts.hjapi.com/jp/2EBB461B55B703F8
simple explain:
 【名词】
   1.常例，惯例。
   2.规章，条例。
   3.例，例子，事例。
 【副词】
   1.经常，通常。
More Detail:
 word attribute: 名词
  1.同種類のものの中から，他を類推させるために，選び出したもの。見本。たとえる。たとえば。例。例子。
    1)例を引く（あげる）。
      举例
    2)彼もそのれいに漏れず。
      他也不例外
    3)例証。
      例证
  2.昔からのならわしで，典拠・標準とするに足るもの。しきたり。習慣。先例。前例。
    1)歴史上に例がない。
      历史上没有先例。
    2)例になっている。
      已成先例。
  3.ならわしになっている。いつもきまっている。定例。惯例。
    1)例のごとし。
      同惯例
    2)例によって。
      和往常一样。按照惯例。
    3)慣例。
      惯例
  4.特別に新しいことでない。いつもと同じ。通常，往常
    1)例の所。
      老地方
    2)例ならず。
      与往常不同
  5.きめられたことがら。規定。条例。规定

零 [れい][rei]① https://tts.hjapi.com/jp/A2D8125D3A745B66
simple explain:
 【名词】
   1.（数量词）零。
More Detail:
 word attribute: 名词
  1.（数量词）零。（記数法で空位を表す；被減数と減数が等しいときの差。ゼロ）。
    1)試合は5対零で負けた。
      比赛以五比零输了。
    2)4に零を掛けてもその答えは零である。
      四乘以零等于零。
'''

# %%
print(match_all(s))