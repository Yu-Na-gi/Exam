# 言語:Python3.10
# 設問:exam_1～4

設問3までは実装できています


## 設問1

exam_1.pyを実行する。
監視ログデータとしてlogfile_1を同ファイル内に準備する。

logfileの監視ログをreadlinesで読み込み、カンマ区切りでlog_separate変数に代入後、
timestamp_str,server_address,response_timeにそれぞれカンマで区切ったデータを代入。
timestamp変数にdatetime.strptime関数を用いてtimestamp_str変数の中身を年月日時分秒のフォーマットに変換する。

もしレスポンス時間がタイムアウト（ハイフン）の場合、故障期間の計測が始まっていない場合には、
故障期間の開始時刻と故障サーバーアドレスを記録し、出力する。
それ以外の場合は、故障期間の計測が既に始まっている場合に、
故障期間を計算して出力し、故障期間の計測をリセットする。


## 設問2

exam_2.pyを実行する。
監視ログデータとしてlogfile_2を同ファイル内に準備する。

設問1のプログラムを拡張し、引数としてタイムアウトの閾値を与え、
タイムアウトした場合にtimeout_countをインクリメントし、そのカウントが
引数で与えた閾値に至った場合に故障とみなし、設問1と同様に記録を始める。

## 設問3

exam_3.pyを実行する。
監視ログデータとしてlogfile_3を同ファイル内に準備する。

設問2のプログラムを拡張し、設問で与えられた直近m回の平均応答時間tを
出力できるように拡張した。
引数として直近の平均応答時間の閾値（今回は15(msec)と設定）と直近m回分の平均応答時間を
保持する変数(今回は５回分)を与えた。

故障期間の計測とは別に応答がタイムアウトしてない場合に、ログから取得した
文字列型の応答時間を整数型に変換し、平均応答時間を計算できるように準備する。

直近5回分のの平均応答時間時間が引数で与えた閾値を超えた場合に過負荷とみなし、
その過負荷の期間とサーバーアドレスを記録し、出力する。


## 設問4
実装できませんでした。
