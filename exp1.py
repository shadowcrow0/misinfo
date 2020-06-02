from psychopy import core, event, gui, visual, data, info

FEEDBACK = []
expInfo = {'age': '', 'gender': ['Male', 'Female'], 'condition': ['1', '2', '3','4'], 'date': '', 'order': ''}
gui.DlgFromDict(dictionary=expInfo, title='retraction', order=['age', 'gender', 'condition', 'date', 'order'])
# Create a visual window:
WIN = visual.Window((1920, 1080), monitor='testMonitor', color="black", units="pix", fullscr=True)

INSTRUCTION = visual.TextStim(WIN, text="請仔細閱讀螢幕中出現的紅字，\n"
                                        "螢幕每次只會呈現一則訊息，\n"
                                        "閱讀完之後請按「空白鍵」，\n"
                                        "將會呈現下一則訊息。\n"
                                        "當你閱讀完所有訊息後，\n"
                                        "接下來需要回達有關訊息的問題。\n"
                                        "實驗進行中如果有任何問題，\n"
                                        "請向主試者詢問。", font="msyh", height=64, pos=[-650, 100])

Q1 = visual.TextStim(WIN, text="為什麼很難區分傷者跟非傷者？",
                     font="msyh", height=64,  color="white", pos=(-650, -100))
Q2 = visual.TextStim(WIN, text="為什麼無論有沒有受傷，\n""乘客都很難離開巴士？", font="msyh", height=64, color="white", pos=(-650, -100))

Q3 = visual.TextStim(WIN, text="警方應該聯繫誰告知乘客意外的經過？", font="msyh", height=64, color="white", pos=(-650, -100))
Q4 = visual.TextStim(WIN, text="為什麼沒有受傷的人也很難從車禍現場站起來？", font="msyh", height=64, color="white", pos=(-650, -100))
Q5 = visual.TextStim(WIN, text="為什麼沒受傷的乘客沒辦法幫助搜救行動？", font="msyh", height=64, color="white", pos=(-650, -100))
Q6 = visual.TextStim(WIN, text="為什麼只有一部分乘客受傷？", font="msyh", height=64, color="white", pos=(-650, -100))
Q7 = visual.TextStim(WIN, text="之後要如何避免這樣的意外發生？", font="msyh", height=64, color="white", pos=(-650, -100))
Q8 = visual.TextStim(WIN, text="為什麼沒受傷的乘客覺得十分無助？", font="msyh", height=64, color="white", pos=(-650, -100))
Q9 = visual.TextStim(WIN, text="為什麼小型巴士會發生車禍？", font="msyh", height=64, color="white", pos=(-650, -100))
Q10 = visual.TextStim(WIN, text="意外發生在哪天？", font="msyh", height=64, color="white", pos=(-650, -100))
Q11 = visual.TextStim(WIN, text="是誰報警？", font="msyh", height=64, color="white", pos=(-650, -100))
Q12 = visual.TextStim(WIN, text="意外後小巴的位置在哪？", font="msyh", height=64, color="white", pos=(-650, -100))
Q13 = visual.TextStim(WIN, text="意外發生在哪裡？", font="msyh", height=64, color="white", pos=(-650, -100))
Q14 = visual.TextStim(WIN, text="意外發生那天，天氣如何？", font="msyh", height=64, color="white", pos=(-650, -100))
Q15 = visual.TextStim(WIN, text="傷者被送到哪個醫院了?", font="msyh", height=64, color="white", pos=(-650, -100))
Q16 = visual.TextStim(WIN, text="有幾位傷者被送到醫院？"
                      , font="msyh", height=64, color="white", pos=(-650, -100))
Q17 = visual.TextStim(WIN, text="沒受傷的乘客在哪裡接受採訪？"
                      , font="msyh", height=64, color="white", pos=(-650, -100))
Q18 = visual.TextStim(WIN, text="在巴士上的是哪些人？"
                      , font="msyh", height=64, color="white", pos=(-650, -100))
Q19 = visual.TextStim(WIN, text="警方的第二分聲明用途是什麼？"
                      , font="msyh", height=64, color="white", pos=(-650, -100))
Q20 = visual.TextStim(WIN, text="你有觀察到聲明哪邊不一樣嗎？"
                      , font="msyh", height=64, color="white", pos=(-650, -100))
Q21 = visual.TextStim(WIN, text="你是否相信更正？還是你覺得其中有發生錯誤？", font="msyh", height=64, color="white", pos=(-650, -100))

INSTRUCT = visual.TextStim(WIN, text="題目出現後，您有15秒的時間可以回答", font="msyh", height=64, color="white", pos=(-650, -100))
NEXT = visual.TextStim(WIN, text="請作答", font="msyh", height=64, color="white", pos=(-650, -100))
TRY = visual.TextStim(WIN, text="描述你住的地方？", height=64, color="white", pos=(-650, -100))
END_TRY = visual.TextStim(WIN, text="練習結束，有問題請發問", height=64, color="white", pos=(-650, -100))
COUNT1 = visual.TextStim(WIN, text="1", height=94, color="white", pos=(650, 300))
COUNT2 = visual.TextStim(WIN, text="2", height=94, color="white", pos=(650, 300))
COUNT3 = visual.TextStim(WIN, text="3", height=94, color="white", pos=(650, 300))
COUNT4 = visual.TextStim(WIN, text="4", height=94, color="white", pos=(650, 300))
COUNT5 = visual.TextStim(WIN, text="5", height=94, color="white", pos=(650, 300))
COUNT6 = visual.TextStim(WIN, text="6", height=94, color="white", pos=(650, 300))
COUNT7 = visual.TextStim(WIN, text="7", height=94, color="white", pos=(650, 300))
COUNT8 = visual.TextStim(WIN, text="8", height=94, color="white", pos=(650, 300))
COUNT9 = visual.TextStim(WIN, text="9", height=94, color="white", pos=(650, 300))
COUNT10 = visual.TextStim(WIN, text="10", height=94, color="white", pos=(650, 300))
COUNT11 = visual.TextStim(WIN, text="11", height=94, color="white", pos=(650, 300))
COUNT12 = visual.TextStim(WIN, text="12", height=94, color="white", pos=(650, 300))
COUNT13 = visual.TextStim(WIN, text="13", height=94, color="white", pos=(650, 300))
COUNT14 = visual.TextStim(WIN, text="14", height=94, color="white", pos=(650, 300))
COUNT15 = visual.TextStim(WIN, text="15", height=94, color="white", pos=(650, 300))
RATE = visual.TextStim(WIN, text="你對這個回答有多少信心？\n"
                                 "1  非常沒信心，\n"
                                 "5  非常有信心。\n"
                                 "請用鍵盤輸入數字！", height=64, color="white", pos=(-650, 100))
class Element(object):
    def __init__(self,a1,a2,a3,a4,a5,a6,a7,a8):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.a8 = a8

class Log(Element):
    def __init__(self,a1,a2,a3,a4,a5,a6,a7,a8):
        super(Log,self).__init__(a1,a2,a3,a4,a5,a6,a7,a8)
    def logData(self): #save data
        dataFile = open("{}_{}_{}_{}.csv".format(expInfo['date'], expInfo['order'], expInfo['age'], expInfo['gender'],expInfo['condition']), 'a')
        dataFile.write('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7,self.a8))

def element_exp():
    INSTRUCTION.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt1 = visual.TextStim(WIN,text="上個星期日，119接到一通電話報告嚴重意外，\n"
                                    "有一輛小型巴士發生一場嚴重車禍。", font="msyh", height=64, color="red", pos=[-650, 100])
    txt1.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt2 = visual.TextStim(WIN, text="報警的人是剛好經過意外現場的駕駛。", font="msyh", height=64, color="red", pos=[-650, 100])
    txt2.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt3 = visual.TextStim(WIN, text="車輛撞上分隔島，\n"
                                     "並且翻滾至對向車道。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt3.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt4 = visual.TextStim(WIN, text="這場意外導致一些乘客受傷。", font="msyh", height=64, color="red", pos=(-650, 100))
    #   txt4.setPos(-2,0)
    txt4.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt5 = visual.TextStim(WIN, text="急救人員在收到通知後，\n"
                                     "立刻前往事故現場。", font="msyh", height=64, color="red", pos=(-650, 100))
    #   txt5.setPos(-2, 0)
    txt5.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt6 = visual.TextStim(WIN, text="救護車大概花十分鐘即抵達事故現場。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt6.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt7 = visual.TextStim(WIN, text="警察說小型巴士的乘客是一群老人，\n"
                                     "事故發生時他們結束里民踏青正要回家。",
                           font="msyh", height=64, color="red", pos=(-650, 100))
    txt7.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt8 = visual.TextStim(WIN, text="根據氣象報告，\n"
                                     " 當天的天氣和能見度皆為良好。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt8.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt9 = visual.TextStim(WIN, text="沒有其他車輛涉入這場意外。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt9.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt10 = visual.TextStim(WIN, text="急救人員嘗試撤離巴士內的乘客，\n"
                                      "但他們沒辦法根據受傷程度將乘客進行分類。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt10.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    WIN.flip()
    txt11 = visual.TextStim(WIN, text="急救人員說當他們清空逃難出口時，\n"
                                      "無論乘客受傷的狀況，\n"
                                      "乘客們都很難離開巴士。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt11.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt12 = visual.TextStim(WIN, text="警方試圖聯絡受傷者的家屬，\n"
                                      "並且根據小巴的車牌號碼追溯巴士的出租業者。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt12.draw()
    WIN.flip()

    event.waitKeys(keyList=['space'])

    txt13 = visual.TextStim(WIN, text="急救團隊表示目前的搜救進度緩慢，\n"
                                      "需要比預期更多時間，\n"
                                      "呼籲旁觀者不要聚集在事故現場。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt13.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt14 = visual.TextStim(WIN, text="救援團隊表示車禍嚴重的程度超出預期，\n"
                                      "以現有的工具很難幫助那些沒受傷的乘客離開巴士。", font="msyh", height=64, color="red",
                            pos=(-650, 100))
    txt14.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt14 = visual.TextStim(WIN, text="當地電台也建議駕駛避開行經仁愛路圓環週邊道路。", font="msyh", height=64, color="red",
                            pos=(-650, 100))
    txt14.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt15 = visual.TextStim(WIN, text="根據電視台報導，\n"
                                      "就算是沒有受傷的乘客也很難從車體離開。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt15.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])

    txt16 = visual.TextStim(WIN, text="救援團隊描述車禍嚴重程度，\n"
                                      "即使是沒受傷的乘客也無法協助救援。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt16.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])


def exp():
    condition = expInfo['condition']
    if condition == '2':
        txt17 = visual.TextStim(WIN, text="根據警方的第二份聲明稿所有乘客都已成功獲救。", font="msyh", height=64, color="red",
                                pos=(-650, 100))
        txt17.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
    elif condition == '1':
        txt17 = visual.TextStim(WIN, text="警方發布第二份聲明表示車上的乘客並非年長者。", font="msyh", height=64, color="red",
                                pos=(-650, 100))
        txt17.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])

    elif condition == '3':
        txt17 = visual.TextStim(WIN, text="警方發布第二份聲明指車上乘客並非年長者，\n"
                                          "而是國中棒球隊員，\n"
                                          "車禍發生在他們贏得比賽後前往慶功宴的路上。", font="msyh", height=64, color="red",
                                pos=(-650, 100))
        txt17.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])
    elif condition == '4':
        txt17 = visual.TextStim(WIN, text="警方發布第二份聲明指車上乘客並非年長者，\n"
                                          "而是國中棒球隊員。", font="msyh", height=64, color="red",
                                pos=(-650, 100))
        txt17.draw()
        WIN.flip()
        event.waitKeys(keyList=['space'])


def statement_after():
    txt18 = visual.TextStim(WIN, text="一些受傷的乘客被送往市立醫院進行治療。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt18.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    txt19 = visual.TextStim(WIN, text="醫院表示除了三名傷者傷勢嚴重須進一步觀察，\n"
                                      "其餘傷者治療後皆已離院。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt19.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])
    txt19 = visual.TextStim(WIN, text="數名未受傷的乘客接受訪談，\n"
                                      "提及車禍當下的無助並由衷的感謝搜救人員的協助。", font="msyh", height=64, color="red", pos=(-650, 100))
    txt19.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])


def instrcution2():
    txt20 = visual.TextStim(WIN, text="接下來請回答問題。", font="msyh", height=64, color="white", pos=(-650, 100))
    txt20.draw()
    WIN.flip()
    event.waitKeys(keyList=['space'])


def rating():
    RATE.draw()
    WIN.flip()
    ans = event.waitKeys(keyList=['1','2', '3', '4', '5'])
    return ans


element_exp()
exp()
statement_after()
instrcution2()
# To do :practice trail : like 3+2 = ? press space to response
def tryit():
    TRY.draw()
    WIN.flip()
    res = event.waitKeys(keyList=['space'])
    print(res)
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "practice.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    TRY.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    TRY.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    TRY.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a0 = rating()
    print(a0)


def q1():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q1.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q1.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q1.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q1.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a1 = rating()
    print(a1)


def q2():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q2.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q2.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q2.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q2.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a2 = rating()
    print(a2)
    return a2


def q3():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q3.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q3.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q3.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q3.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a3 = rating()
    return a3


def q4():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q4.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q4.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q4.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q4.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a4= rating()
    print(a4)

    return a4

def q5():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q5.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)


    Q5.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q5.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q5.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a5 = rating()
    print(a5)
    return a5

def q6():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q6.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q6.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q6.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q6.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a6 = rating()
    print(a6)
    return a6


def q7():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q7.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q7.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q7.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q7.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    a7 = rating()
    print(a7)
    return a7


def q8():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q8.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q8.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q8.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q8.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a8 = rating()
    print(a8)
    return a8


def q9():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q9.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q9.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q9.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q9.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a9 = rating()
    print(a9)
    return a9


def q10():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q10.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q10.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q10.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q10.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a10 = rating()
    print(a10)
    return a10


def q11():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q11.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q11.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q11.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q11.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a11 = rating()
    print(a11)
    return a11

def q12():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q12.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q12.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q12.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q12.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a12 = rating()
    print(a12)
    return a12


def q13():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q13.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q13.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q13.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q13.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a13 = rating()
    print(a13)
    return a13


def q14():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q14.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q14.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q14.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q14.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a14 = rating()
    print(a14)
    return a14


def q15():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q15.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    Q15.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q15.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q15.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a15 = rating()
    print(a15)
    return a15


def q16():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q16.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q16.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q16.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q16.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a16 = rating()
    print(a16)
    return a16


def q17():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q17.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q17.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q17.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q17.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a17 = rating()
    print(a17)
    return a17


def q18():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q18.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q18.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q18.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q18.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a18 = rating()
    print(a18)
    return a18


def q19():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q19.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q19.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q19.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q19.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a19 = rating()
    print(a19)
    return a19


def q20():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q20.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q20.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q20.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q20.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a20 = rating()
    print(a20)
    return a20


def q21():
    import pyaudio
    import wave

    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 15
    filename = "Q21.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    Q21.draw()
    COUNT1.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT2.draw()
    WIN.flip()
    core.wait(1)
    COUNT3.draw()
    Q21.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT4.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT5.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT6.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT7.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT8.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT9.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT10.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT11.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT12.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT13.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT14.draw()
    WIN.flip()
    core.wait(1)
    Q21.draw()
    COUNT15.draw()
    WIN.flip()
    core.wait(1)
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    a21 = rating()
    print(a21)
    return a21


# practice()

def order():

    a1 = q1()
    a2 = q2()
    a3 = q3()
    a4 = q4()
    a5 = q5()
    a6 = q6()
    a7 = q7()
    a8 = q8()
    a9 = q9()
    a10 = q10()
    a11 = q11()
    a12 = q12()
    a13 = q13()
    a14 = q14()
    a15 = q15()
    a16 = q16()
    a17 = q17()
    a18 = q18()
    a19 = q19()
    a20 = q20()
    a21 = q21()
    print(expInfo['date'], expInfo['order'], expInfo['age'], expInfo['gender'],expInfo['condition'])
    print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21)




def logData():  # save data
    dataFile = open("{}_{}_{}_{}.csv".format(expInfo['date'], expInfo['order'], expInfo['age'], expInfo['gender'],
                                             expInfo['condition']), 'a')

tryit()
order()

