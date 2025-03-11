def winstreak(poin_slayer, win_streak, poin_ws):
    if win_streak == 1:
        print ("bukan win streak")
    else:
        for i in range (0,win_streak):
            poin_slayer += poin_ws
            poin_ws += 100
        print(f'saya punya poin: {poin_slayer}')
    
winstreak(1000,3,100)
winstreak(0,1,100)