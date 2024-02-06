# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:18:29 2024

@author: nagi_
"""

from datetime import datetime

def watch_log(log_file, timeouts_threshold):
    with open(log_file, 'r') as file:
        lines = file.readlines()

    timeouts_count = 0 #タイムアウトした回数を記録する
    failure_start_time = None #故障開始時間
    failure_server_address = None #故障したサーバーアドレス

    for line in lines:
        #ログをカンマで分割
        log_separate = line.strip().split(',')
        #ログの各要素を取得
        timestamp_str, server_address, response_time = log_separate
        timestamp = datetime.strptime(timestamp_str, '%Y%m%d%H%M%S')
        
        
        
        if response_time == '-': #レスポンス時間が '-'（ハイフン）の場合、タイムアウトと見なす
            timeouts_count += 1
            #連続タイムアウトカウンとが指定した閾値を超えた場合
            if timeouts_count >= timeouts_threshold:
          
                # 故障期間の計測がまだ始まっていない場合
                if not failure_start_time:
                    failure_start_time = timestamp #故障が始まった時間を記録
                    failure_server_address = server_address #故障が始まったサーバーアドレスを記録
                    
        else: #レスポンス時間が'-'でない場合
            timeouts_count = 0
            #既に故障期間の計測が始まっている場合(failure_start_timeがNoneでない場合)
            if failure_start_time:
                failure_duration = timestamp - failure_start_time
                print(f"故障サーバ: {failure_server_address}, 故障期間: {failure_duration}")
                #故障期間の計測をリセット
                failure_start_time = None
                failure_server_address = None




#連続タイムアウト回数 N を指定してプログラムを実行
log_file = 'logfile_2.txt'
timeouts_threshold = 3 #3回以上連続でタイムアウトした場合に故障とみなす
watch_log(log_file, timeouts_threshold)
