# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:39:10 2024

@author: nagi_
"""

from datetime import datetime

def watch_log(log_file_path, timeouts_threshold, recent_average_threshold, recent_average_count):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    timeouts_count = 0 #タイムアウトした回数を記録する　
    failure_start_time = None #故障開始時間
    failure_server_address = None #故障したサーバーアドレス

    recent_response_times = [] #直近の応答時間を保持するリスト
    overload_start_time = None #過負荷状態開始時間
    overload_server_address = None #過負荷状態のサーバーアドレス

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
                
                #故障期間の計測がまだ始まっていない場合
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

            response_time = int(response_time) #文字列型の応答時間を整数型に変換する
            recent_response_times.append(response_time) #整数型に変換された応答時間をリストに追加する

            if len(recent_response_times) > recent_average_count: #リストの要素数が引数で与えた閾値を超えた場合
                recent_response_times.pop(0)  # リストの先頭を削除して保持数を制限

            #リスト内の応答時間の合計を計算し、平均値を求める（直近の平均応答時間）
            recent_average = sum(recent_response_times) / len(recent_response_times) 
            
            if recent_average > recent_average_threshold: #直近の平均応答時間が閾値(15)を超えた場合
                #過負荷状態の計測がまだ始まってない場合
                if not overload_start_time: 
                    overload_start_time = timestamp #過負荷が始まった時間を記録
                    overload_server_address = server_address #過負荷が始まったサーバーアドレスを記録
            else:
                if overload_start_time: #過負荷の計測が始まっている場合
                    overload_duration = timestamp - overload_start_time #過負荷の期間を計測する
                    print(f"過負荷サーバ: {overload_server_address}, 過負荷期間: {overload_duration}")
                    #過負荷期間の計測をリセット
                    overload_start_time = None
                    overload_server_address = None

    #ログファイルの最後で過負荷状態が続いている場合
    if overload_start_time: #過負荷の計測が始まっている場合
        overload_duration = timestamp - overload_start_time #過負荷の期間を計測する
        print(f"過負荷サーバ: {overload_server_address}, 過負荷期間: {overload_duration}")

# パラメータとして連続タイムアウト回数 N、直近の平均応答時間の閾値 T、保持する平均応答時間の回数 M を指定してプログラムを実行
log_file_path = 'logfile_3.txt'
timeouts_threshold = 3 #3回以上連続でタイムアウトした場合に故障とみなす
recent_average_threshold = 15 #直近の平均応答時間が15ミリ秒を超えた場合に過負荷とみなす
recent_average_count = 5 #直近の平均応答時間を5回分保持する
watch_log(log_file_path, timeouts_threshold, recent_average_threshold, recent_average_count)
