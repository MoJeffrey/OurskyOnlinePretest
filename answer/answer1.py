import re


def GetMostWordsString(StrList: list) -> str:
    """
    Find most words
    :param StrList: String List
    :return: most words string
    """
    MostWordsString = ''
    MostWordsNum = 0
    for Words in StrList:
        NowWordsNum = len(re.findall(r'[A-Z][\[a-z]+|[A-Z]+|[]]', Words))

        if MostWordsNum > NowWordsNum:
            continue

        elif MostWordsNum == NowWordsNum:
            if len(StrList) > len(MostWordsString):
                MostWordsString = Words

        else:
            MostWordsString = Words
            MostWordsNum = NowWordsNum

    return MostWordsString


if __name__ == '__main__':
    Dictionary = ["Hi", "Hello", "HelloWorld", "HiWorld", "HelloWorldWideWeb", "HelloWWW"]
    Output = "HelloWorldWideWeb"
    print(GetMostWordsString(Dictionary))

    Dictionary = ["Oursky", "OurSky", "OurskyLimited", "OurskyHK", "SkymakersDigitalLTD", "SkymakersDigitalLtd"]
    Output = "SkymakersDigitalLTD"
    print(GetMostWordsString(Dictionary))
