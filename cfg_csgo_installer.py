import os
import msvcrt
def cfginstall():
    print('Version 1.0 - practice cfg for csgo installer by Sim')
    print('https://steamcommunity.com/id/SimonMorales/')
    print('')
    path=input('Insert the path where the game is located (Counter-Strike Global Offensive): ')
    while os.path.exists(path)==False:
        path=input('The path is incorrect. Insert the path where the game is located: ')
    else:
        print('The current location of the game is correct...')
        rushure=input('The cfg is going to be installed in that location. Are you shure? (y/n): ')
        while rushure!='y' and rushure!='n':
            rushure=input('***Wrong, you have to use y for yes or n for not***. The cfg is going to be installed in that location. Are you shure? (y/n): ')
        else:
            if rushure=='y':
                newpath=path+'\csgo\cfg\practice.cfg'
                file=open(r'{}','w'.format(newpath))
                file.write('sv_cheats 1;mp_limitteams 0;bot_kick;mp_freezetime 0;mp_roundtime 60;mp_buy_anywhere 1;mp_buytime 99999;mp_startmoney 30000;sv_infinite_ammo 2;sv_grenade_trajectory 1;sv_grenade_trajectory_time 10;mp_roundtime_defuse 60;mp_roundtime_hostage 60;mp_restartgame 1;sv_showimpacts 1;bot_stop 1;cl_cmdrate 128;cl_updaterate 128;mp_respawn_on_death_t 1;mp_respawn_on_death_ct 1;ammo_grenade_limit_total 10;bind "z" sv_rethrow_last_grenade;bind "x" bot_place;bind "v" noclip;mp_warmup_end')
                file.close()
                print('')
                print('cfg created succesfully!')
                print('The name of the cfg is practice.cfg')
                print('')
                print("Tap any key to close")
                msvcrt.getch()
            if rushure=='n':
                print("Tap any key to close")
                msvcrt.getch()
cfginstall()    