# Создайте программу для игры в ""Крестики-нолики"".

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def playing_field(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def gamer(player):
   valid = False
   while not valid:
      player_reply = input("Куда поставим " + player+"? ")
      try:
         player_reply = int(player_reply)
      except:
         print("Некорректный ввод. Введите число от 1 до 9.")
         continue
      if player_reply >= 1 and player_reply <= 9:
         if(str(board[player_reply-1]) not in "XO"):
            board[player_reply-1] = player
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in win_coord:
       if board[i[0]] == board[i[1]] == board[i[2]]:
          return board[i[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        playing_field(board)
        if counter % 2 == 0:
           gamer("X")
        else:
           gamer("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    playing_field(board)
main(board)



