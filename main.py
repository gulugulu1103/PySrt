import os

def generate_srt(start_times, end_times, lyrics, translates=None, output_file='output.srt'):
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, (start, end, lyric) in enumerate(zip(start_times, end_times, lyrics)):
            if translates:
                translated_lyric = translates[i]
            else:
                translated_lyric = ""
            
            f.write(f"{i+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{lyric}\n")
            if translated_lyric:
                f.write(f"{translated_lyric}\n")
            f.write("\n")

if __name__ == '__main__':
    start_times = [
    "00:00:18.200",
    "00:00:23.900",
    "00:00:30.400",
    "00:00:36.100",
    "00:00:43.000",
    "00:00:49.000",
    "00:00:55.100",
    "00:01:01.300",
    "00:01:07.700",
    "00:01:19.450",
    "00:01:25.200",
    "00:01:31.600",
    "00:01:37.200",
    "00:01:43.900",
    "00:01:47.180",
    "00:01:49.450",
    "00:01:53.300",
    "00:01:56.600",
    "00:02:02.400",
    "00:02:08.500",
    "00:02:14.650",
    "00:02:21.050",
    "00:02:48.300",
    "00:02:54.400",
    "00:03:00.500",
    "00:03:06.650",
    "00:03:13.000",
    "00:03:18.850",
    "00:03:25.100",
    "00:03:31.000"
]

    end_times = [
    "00:00:23.900",
    "00:00:30.400",
    "00:00:36.100",
    "00:00:43.000",
    "00:00:49.000",
    "00:00:55.100",
    "00:01:01.300",
    "00:01:09.300",
    "00:01:19.450",
    "00:01:25.200",
    "00:01:31.600",
    "00:01:37.200",
    "00:01:43.900",
    "00:01:47.180",
    "00:01:49.450",
    "00:01:53.300",
    "00:01:56.600",
    "00:02:02.400",
    "00:02:08.500",
    "00:02:14.650",
    "00:02:21.050",
    "00:02:45.968",
    "00:02:54.400",
    "00:03:00.500",
    "00:03:06.650",
    "00:03:13.000",
    "00:03:18.850",
    "00:03:25.100",
    "00:03:31.000",
    "00:03:40.220"
]

    lyrics = [
    "ねぇ、どっかに置いてきたような",
    "事が一つ二つ浮いているけど",
    "ねぇ、ちゃんと拾っておこう",
    "はじけて忘れてしまう前に",
    "回り出した あの子と僕の未来が",
    "止まりどっかで またやり直せたら",
    "回り出した あの子と僕が被害者",
    "づらでどっかを また練り歩けたらな",
    "とぅるるる とぅるるる とぅるる",
    "あのね、私あなたに会ったの",
    "夢の中に置いてきたけどね",
    "ねぇ、どうして私が好きなの",
    "一度しか会ったことがないのにね",
    "思いを蹴って 二人でしてんだ",
    "壊(わす)れない愛を歌う",
    "言葉を二人に課して 誓いをたてんだ",
    "忘れない愛を歌うようにね",
    "回り出した あの子と僕の未来が",
    "止まりどっかで またやり直せたら",
    "回り出した あの子と僕が被害者",
    "づらでどっかを また練り歩けたらな",
    "とぅるるる とぅるるる とぅるる",
    "回り出した あの子と僕の未来が",
    "止まりどっかで またやり直せたら",
    "回り出した あの子と僕が被害者",
    "づらでどっかを また練り歩けたらな",
    "時代に乗って僕たちは 変わらず愛に生きるだろう",
    "僕らが散って残るのは 変わらぬ愛の歌なんだろうな",
    "時代に乗って僕たちは 変わらず愛に生きるだろう",
    "僕らが散って残るのは 変わらぬ愛の歌なんだろうな"
]

    translates = [
    "嘿，過去遺留在某處的往事",
    "一件兩件在記憶中浮現",
    "吶，好好地把它們撿回來吧",
    "在腦容量塞爆 忘的一乾二淨之前",
    "開始轉動 那女孩和我的未來",
    "在某處停了下來 要是能再重來一遍",
    "開始轉動 要是那女孩能和我一起裝作",
    "被害人的樣子 再次結伴向前行就好了啊",
    "",
    "跟你說，我遇到了你喔",
    "只是把你留在我的夢裡面了",
    "吶，你為什麼會喜歡我呢",
    "明明我們也只見過一次面而已",
    "踢著自己的感情 我們兩個人這樣做",
    "歌頌著永不會壞(忘)的愛",
    "將話語加諸於兩人身上 立下誓言",
    "要唱著永不忘記的愛",
    "開始轉動 那女孩和我的未來",
    "在某處停了下來 要是能再重來一遍",
    "開始轉動 要是那女孩能和我一起裝作",
    "被害人的樣子 再次結伴向前行就好了啊",
    "",
    "開始轉動 那女孩和我的未來",
    "在某處停了下來 要是能再重來一遍",
    "開始轉動 要是那女孩能和我一起裝作",
    "被害人的樣子 再次結伴向前行就好了啊",
    "與時俱進 我們依然還是會依靠著愛活下去的吧",
    "我們分崩離析所剩下的是恆久不變的愛所譜出的歌嗎",
    "與時俱進 我們依然還是會依靠著愛活下去的吧",
    "我們分崩離析所剩下的是恆久不變的愛所譜出的歌嗎"
]
    # Generate the srt file
    generate_srt(start_times, end_times, lyrics, translates, 'output.srt')
