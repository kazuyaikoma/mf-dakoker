[![PyPI](https://img.shields.io/pypi/v/dakoker.svg)](https://pypi.python.org/pypi/dakoker)

MF-Dakoker
=======

[MFクラウド勤怠](https://biz.moneyforward.com/attendance)利用者向けに作った打刻・勤怠状況確認ツールです。

主な機能
- MFクラウド勤怠へのログイン, 出勤・退勤の打刻

実装予定機能
- 休憩時間の打刻
- 二重打刻の防止機能
- 過去・当日の勤怠状況の確認(打刻日時)

動作環境
- Python 3.8以降

## How to Install
`pip3 install dakoker`

## Usage

- 出勤
  - `dakoker start`
- 退勤
  - `dakoker stop`
