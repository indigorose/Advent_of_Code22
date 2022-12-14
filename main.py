from pandas import *
from itertools import groupby
import re

# ---- Imported sheets ---- #

data = read_csv("elves_calories - Sheet1.csv")
hands_dealt = read_csv("Advent of Code - Sheet3.csv")
rucksacks_data = read_csv("Advent of Code - Sheet2.csv")
cleanup_data = read_csv("Advent of Code - Sheet4.csv")
moves_data = read_csv("Advent of Code - Sheet5.csv")

# ---- Day 1 - Calorie Counting ---- #

"""If you ever have tons of data, try reading through pandas to convert to a list.
There are some ways to add break or special characters to break the list if you require nested loops."""

# Part one - the highest total number of calories for an elf.
calories = data['calories'].tolist()
# print('calories', calories)

new_list = [list(g) for key, g in groupby(calories, lambda x: x == 'Break') if not key]
# print(new_list)

elves = [[int(calorie) for calorie in sub_list] for sub_list in new_list]

total_cal = [sum(elf) for elf in elves]
# print(total_cal)
answer = max(total_cal)
# print(answer)
# print(total_cal.index(answer))

# Part two - The total of the top three elves with the highest calorie count
total_cal.sort(reverse=True)
# print(total_cal)

top_3 = sum(total_cal[0:3])
# print(top_3)

# ---- Day 2 - Rock Paper Scissors ---- #
hands_list = hands_dealt["Hands_dealt"].tolist()
# print(hands_list)
hands_pos = {"Rock": ["A", "X", 1],
             "Paper": ["B", "Y", 2],
             "Scissors": ["C", "Z", 3],
             }
# Scoring
score = {"Lost": 0,
         "Draw": 3,
         "Win": 6,
         }
# Play combinations
pos_combinations = {
    "Win": [["C X", 7], ["A Y", 8], ["B Z", 9]],
    "Draw": [["A X", 4], ["B Y", 5], ["C Z", 6]],
    "Lost": [["B X", 1], ["C Y", 2], ["A Z", 3]],
}


# print(pos_combinations["Win"][0][1])


# Combination to win
def total_score(hands):
    count = 0
    for hand in hands:
        if hand == pos_combinations["Lost"][0][0]:
            count += 1
        elif hand == pos_combinations["Lost"][1][0]:
            count += 2
        elif hand == pos_combinations["Lost"][2][0]:
            count += 3
        elif hand == pos_combinations["Draw"][0][0]:
            count += 4
        elif hand == pos_combinations["Draw"][1][0]:
            count += 5
        elif hand == pos_combinations["Draw"][2][0]:
            count += 6
        elif hand == pos_combinations["Win"][0][0]:
            count += 7
        elif hand == pos_combinations["Win"][1][0]:
            count += 8
        elif hand == pos_combinations["Win"][2][0]:
            count += 9
        else:
            count += 0
    return count


# print(total_score(hands_list))

x = "lose"
y = "draw"
z = "win"

combinations = {
    "lose": [["B X", 1], ["C X", 2], ["A X", 3]],
    "draw": [["A Y", 4], ["B Y", 5], ["C Y", 6]],
    "win": [["C Z", 7], ["A Z", 8], ["B Z", 9]]
}


# ---- Part two answer to Day 2 ---- #
def lose_count(hands):
    count = 0
    for hand in hands:
        if hand == combinations["lose"][0][0]:
            count += 1
        elif hand == combinations["lose"][1][0]:
            count += 2
        elif hand == combinations["lose"][2][0]:
            count += 3
        elif hand == combinations["draw"][0][0]:
            count += 4
        elif hand == combinations["draw"][1][0]:
            count += 5
        elif hand == combinations["draw"][2][0]:
            count += 6
        elif hand == combinations["win"][0][0]:
            count += 7
        elif hand == combinations["win"][1][0]:
            count += 8
        elif hand == combinations["win"][2][0]:
            count += 9
        else:
            count += 0
    return count


# print(lose_count(hands_list))

# ---- Day 3 - Rucksack Reorganization ---- #

# Create alphabet counting list
alphabet_count = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                  'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
                  'x': 24, 'y': 25, 'z': 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34,
                  "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45,
                  "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52
                  }
# Create list from csv data
rucksacks = rucksacks_data["Rucksacks"].tolist()
# print(rucksacks)

# Split and prepare the list for function manipulation
r_list = []

for sack in rucksacks:
    s1 = sack[:len(sack) // 2]
    s2 = sack[len(sack) // 2:]
    r_list.append(s1)
    r_list.append(s2)

# print(r_list)
sack_list = [r_list[i:i + 2] for i in range(0, len(r_list), 2)]


# print(sack_list)


# Create function to review nested sacks for common letters and store in list to score later
def split_sack(sacks):
    letters = []
    f_score = 0
    for s_sack in sacks:
        letter = [i for i in s_sack[0] if i in s_sack[1]]
        # print(letter)
        letters.append(letter)
    # print(letters)
    for letter in letters:
        f_score += alphabet_count[letter[0]]
    return f_score


# print(split_sack(sack_list))


# ---- Day 3 - Part two ---- #
# Split into three and prepare the list for function manipulation
def three_split(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


three_list = list(three_split(rucksacks, 3))


# print(three_list)


def sp_sack(sacks):
    new_letter = []
    t_score = 0
    for t_sack in sacks:
        letter = [char for char in t_sack[0] if char in t_sack[1] and char in t_sack[2]]
        new_letter.append(letter)
    # print(new_letter)
    for letter in new_letter:
        t_score += alphabet_count[letter[0]]
    return t_score


# print(sp_sack(three_list))


# ---- Day 4 - Camp Cleanup - Part one ---- #

cleanup_range = cleanup_data["cleanup_sections"].tolist()
# print(cleanup_range)

nested_range = [re.split(r'[-,]', item) for item in cleanup_range]
# print(nested_range)

nested_range = [list(map(int, x)) for x in nested_range]


# print(nested_range)


def check_cleanup(nested_range_list):
    count = 0
    for n_range in nested_range_list:
        if n_range[1] >= n_range[3] and n_range[0] <= n_range[2]:
            count += 1
        elif n_range[3] >= n_range[1] and n_range[2] <= n_range[0]:
            count += 1
        else:
            count += 0
    return count


# print(check_cleanup(nested_range))


# ---- Day 4 - Part 2 ---- #

def check_overlap(nested_range_list):
    count = 0
    for n_range in nested_range_list:
        if n_range[3] >= n_range[0] and n_range[1] >= n_range[2]:
            count += 1
        elif n_range[0] >= n_range[3] and n_range[2] >= n_range[1]:
            count += 1
        else:
            count += 0
    return count


# print(check_overlap(nested_range))


# ---- Day 5 - Supply Stacks - Part one ---- #
moves = moves_data['Moves'].tolist()
# print(moves)
moves = [re.findall(r'\b\d+\b', move) for move in moves]
# print(moves)
moves = [list(map(int, x)) for x in moves]
# print(moves)
stacks = {
    1: ["R", "G", "H", "Q", "S", "B", "T", "N"],
    2: ["H", "S", "F", "D", "P", "Z", "J"],
    3: ["Z", "H", "V"],
    4: ["M", "Z", "J", "F", "G", "H"],
    5: ["T", "Z", "C", "D", "L", "M", "S", "R"],
    6: ["M", "T", "W", "V", "H", "Z", "J"],
    7: ["T", "F", "P", "L", "Z"],
    8: ["Q", "V", "W", "S"],
    9: ["W", "H", "L", "M", "T", "D", "N", "C"]
}

# def move_crates(a, b, c, stacks):
#     m_stack = stacks[b][-a:]
#     m_stack.reverse()
#     print(m_stack)
#     stacks[c].extend(m_stack)
#     stacks[b] = stacks[b][0:-a]
#     print(stacks)
#
#
# for move in moves:
#     move_crates(move[0], move[1], move[2], stacks)
#
#
# for key in stacks:
#     print(stacks[key][-1])


# ---- Day 5 - Part two ---- #

# def reverse_crates(a, b, c, stacks):
#     r_stack = stacks[b][-a:]
#     print(r_stack)
#     stacks[c].extend(r_stack)
#     stacks[b] = stacks[b][0:-a]
#     print(stacks)
#
#
# for move in moves:
#     reverse_crates(move[0], move[1], move[2], stacks)
#
#
# for key in stacks:
#     print(stacks[key][-1])


# ---- Day Six - Tuning Trouble - Part one ---- #

# string = "mqllsjlslffbqbsbpbcbdbfbfvbfblfltffpddsmmhjmjvmvsmvvjfvfjjfccblbddhrdhrrlcrllrrswwlpwlwwgrglrgllrrlsshffrwfwcffmrrdfdrrncrnnlvllbsbcbwcchsshsrhhbnhbbqbmmmfdfvvqpqlpqppfgpfgpfpfttwrwwwfmfpfpmmpgglwglgfgsfgsggdllfhhmchmhttlhlchhrzrszsqqqzdzrrbbpgpccmfcmcbcdcrdrzzvjjgjfgfqfcqffvbbjbjbjsbjjbhjjzjlzjznzbbjvvpssdfdvffssrffpzfppsddgwgzgccrmrmdrrzpzbbjlbjlbjbgjbjmmtmllqffpjfppzzztfzfzfmfnndmdtmmhgmmsdshdhppbnpnbpnpdndgdbdwdtwwzqqjwjpphnnjddlglzlczzdpdjdjtjtgtqtptrrbqqqspsfswsdwdjdsdcdllpzpqplqqjnjrnnvrrnrccnwnnsttqzqcqppvmvdmdjjpnppljppptpzzwbwrrqgqhghshlslblflhflfbbwhwlhwhbwbdwbdwwzlwzwhzwznwwmmrddlttdrtrsttqbqtqtdqttqwwglwlbbdmbmcbbwbnbtbmbggdqqnhqqptpdtttvcvmvmdmtdttcwclccjcrctcllrprlrqqzqccttgnntstrtqqtfthtghhvcczhhctclljcljlcjcdjcdchhmjmjjrsjszjszsbsqqpfflqffqvfqvqjjnjtthvvvcjcjrcjclcwcrcrjcrchrcrggcjjpjjbwjbwjbwjwsjjrssfggzbgzgzrzmrmwmrrczcppnmnmzzgtglljlhjlhhgzgtgddrrhvvvlhlwhlhzzgzfgzzbvbvrvllplnlqnnfvnvgvdgvddsdqsdscscjjjvrvpptgpgdgtdtdzdtztfzfszfftjftfmftmtftddjzdzssfllfsllpwpwswrwdrwrcclczlclpccdrrftrftrtltftnftfnfrnfrfgfjfttrsrqsshlhdhnnztntwwnwppwbbmrbbtntznzggthghfggttpnpnpbplpvvpmmpwmbgcpwgsfndbrclcwbdcfhlcqblplglnqpnrpjqbddfqlqvbzrtwbwzvwqntcgmzrzztlffzmfmcmfzrmcvfctmlrlbtbpsgddbqrlblsslsbcmcglzdzjzlpgzprbrmfmlzrssqddzfjzfgbpvdgrrnldmtqgtjppqqwtzbltpfgpqtdqpwhbbwblnvvpmnljdghwrbnphswhgcvhpcplbbmwprznzzwnfntfplscpflhwdmlvfwtgrjhchnmnqbfgvsglllnnzwchqtcrvqzzhttcmblcthqrjdbvpwptcqtsnwrnfbbsqlshhtqdvcfcgdlbgzqjvzvglbcdwzpzttjnsvwrdldcqqstnnfnjthncgfvggphgfgstnmvnbmtvhpmsgmrccmmslqmjfzdjnbcjbjnpmsnvmzrphhjrdrrssnclvwbnzvpccqglnpljdtwrlnvpqzlshpcmfnmrjchqvlmthqbdrlnnpwcmfnwfzpbpnrsdmrqgqsjgwttwhgqlwghjntrvdndfhdwfzbwnmbjlzbhhdqfrdtwcjjvfnjbqdmdwncfhmslflvhqdmrcdrcdrldnqdmhzsvlglgflmlhwjqvfjdmqbmgffvdmmsbrrnrlcsbncvsjffttmhnbpwmqrnvdmzhztbbsrtwgfshjnlvhqvzwpvrmqfbsszswvrglnmwlmcdpjvmqsgnjshspzwrwctwwghmgjvbthcqcrlflsnrnpwvbnghrhvzpzchjlcljplflzqdvglgtvczhnbnlqltblddslqmdpvfbstvszqdsjvgfqlmdgbsnlzlrnbbqqfqjfqhljzlpbbgbnchwljjcpzbhdmwfzmqstcwtvgtvwcpgvmhpsngrshjvzzngbhjqmcfgjjzgdzcsbsvfwmznmwnnvlbntvcmgphqmdfjvhrlldcpwgnmbpjlqflvsrwqphvlpzlsdthfzdzvlphzdbqldvggsgrcmmfmfnjsfszqqbhnmntfgrbfwtlpqgwnrcqdsmqpqbtfdsnhbdcbwcdrhrfgsctrnlchrrnlptbcnqhndcpcdrgtznqrbgjlwzsjhblptncwtqcqcbzccrnjcmfvfnzwlrgdtgcvvcprwvnrrbdjzfnlvlqfpgbpwsvcnmnmmhnshtjgrcnscljwncdjqtwhlhvcggnwbzlzvfqmcdhmzddrdhvnnjbzbtnrgqcbmzhzzfldhlwwsgztfhncgctvjvszdzhrqmzvffmhvsqssjjvrrmtwqswhwjqgbfghbgfmgqssfhbcrglnbstfnqzvwqcznzgtnvjdvhtrlmgthcrqcwbjnzddsqhzwmdwndqcplhvpbpsdthngqwmlfqfndfqbpbwwrvsrnsjbsrwjdjbcqcvdfcsscgblggwggtmbntnbmmswfhvzhltwvprdgvzwltchhzsqlpwdndwftmsgbfwbpmhsdjhwbvvpzlpspsrsnpbwtdspfvdqdjfjbzmmtbnpzrqngccrbfndnjbcjfvwjvfjdvmsqdvgctzvpzmjmjvggpqfmmrsvqbrrlwrmzhmhpcmpltwdbtmwgzrrvsdhvhlwzggjwqzpbzvzrdbptzhzcrrjwjmdwdpsfwfspjgtmfcvddgspldbldtbtwrzdsjrbhvvcjgnrsbzvbrnqjwhrzgfsbdjlfqlszvlnrbfcrgfwrsmqmmnrwbtvfdpjzpfbhplfdsrwwgqqtgnzvddbgjjllmmcjjlglwmsbwrdrnnznwzplnbhlrlnmnllwgwgdpqdqqlmvsbgcshsmntrrlrvdhjgctzsfhmvfqtthvvchftflhlqqhhhbhqvgwtcmgcfwldhgptfddpsqrfzqmtpszswfrztzfsspltcvjwwsljsnjpnnqggscwwmcwfrljlrtqwqvplthsctvbndjfpnvcbdngzqtgjvwlsdhthdwmjvtnzrplwzwsfmgszpqjcjttslsmtbbvhjgpqmqfjbcccsnrlwmjhbsqgzqldmlhnbjnjfwmgzpvdcwndbwcncmtzccngcghhpwmjnncfgqtdtzwmhbdrpwsfbnjzfnwzwqncnlfjqjrjhgnqgvbcdhgdnbwpqjcfgprmfhzlrqtwlqpshfrgdszrwdtqfcntrzbgzlvrhtlsbjjwtnlqllnsvbzwjlmqvdgvtslmbwwcfstmqntwwwsjmrflrqnttfzjchpgwczzdtqbhdrtrpvhhbscvjtdtrhbstpqrnrzszwvcqzhbrzhlblvzrgwtqzbslbmgdqhpfqrdqrzcsbglcsshcwvlcpgjtjmcgpmsnldjzlwnrqlzzznpvmgssvzshjvtsmmzvstpqrhfvttnsrddfcqcbwhgpfdtlhcvcgjgdrvvntvdjqpvwvfmphhpzjgmshddqfsbpjbzrfdjnwrhmgcfbccmzqgvrbmcjdpvwfrtdpbwvjtjcrmnpzrrqbbvbsgcplwmlbsdwptbprlczjcqhdzprpttvnthbmtscdtjvrnwqhnvqbzvwnphnzwlgvvjhddjvjrvwlmhqcsffcnhgjzdjppqqwbglbhgzsmvzwjdvbqpztphshtrbrrhzmdlfdtssbhrcltwlqpzvpgbsgngpfjsjbrnnlzctqcqzwswhfnjjngwsztdgmmcffqfhbsgwstnflqjqttzbtgjvcfrrdwzcvhwjnhmtphszrsptjsqqwcwfnmtlzvzsqsmghtztrpvdslrmjqqvwfmzlwwjbwtpmhtqcfctdztsnfrhfqwqcjdzmjhvwwgrslmdqqwgwfvwlzzsznmdrzgcvbmrtcvjsqlftnpdhwmrzjwsnjjdrczbjcwhwlrtljwjsfmcfcrsjflsldbjrzpdgltmhtszzznjjlfqmgpbjfjncvtvlcfsmltbsvsrgdhwwhcpbdbntqhgjztvlwtwdsgqfwtlcdzffcszjmjvj "

# starting four
# check_list = []
# for i in range(0, len(string), 1):
#     check_str = string[i: i + 4]
#     check_list.append(check_str)
#
# print(check_list)
# answer = []
#
# for check in check_list:
#     if len(set(check)) == len(check):
#         answer.append(check)
#
# print(answer)
#
# print(string.index(answer[0]) + 4)


# ---- Part two ---- #

# check_list = []
# for i in range(0, len(string), 1):
#     check_str = string[i: i + 14]
#     check_list.append(check_str)
#
# print(check_list)
# answer = []
#
# for check in check_list:
#     if len(set(check)) == len(check):
#         answer.append(check)
#
# print(answer)
#
# print(string.index(answer[0]) + 14)


# ---- Day 7 - No Space Left on Device ---- #

