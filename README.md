# Deepl-DiscordBOT

これはDeepl翻訳を用いてDiscordのテキストメッセージを日本語から英語、もしくは英語から日本語へ翻訳するDiscord Botです<br>
※本スクリプトは個人利用レベルのものであり、第三者による利用を深く想定していません。予めご了承ください

## 機能
* テキストメッセージに絵文字リアクションを付与すると、翻訳結果をDMに返します
* トリガーとなる絵文字はconfigから変更することが可能です
* BOTが参加しているサーバの全てのチャンネルと、BOTとのDM上のメッセージを翻訳することができます

## 動作デモ
![Demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW0xNmEyMzN4dG1vcmFnOWV1MmhpbG90a3Jtd3duaXpkbGV3dHBqeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/J7lRlSAEOZFRpkqp1B/giphy.gif)

## セットアップと起動
※python、Discord.pyの導入などは割愛

1. 当リポジトリから`deepl.py`と`config.ini`をDLし、同じ階層にまとめる
1. `config.ini`にDiscoed botトークンとDeepl API KEYをセットする
    * Deepl APIはFree版のみを想定しています
1. （必要に応じて）`config.ini`にトリガーとなる絵文字を設定する
    * デフォルトでは、日本語→英語の翻訳には「🇯🇵」、英語→日本語の翻訳には「🇺🇸」が設定されています
1. deepl.pyを叩く

## サーバへの招待と使い方

1. 機能を利用したいサーバへbotを招待します
    * discord developer portalでOAuth2 URL Generatorを使用し招待します<br>
    このとき、**スコープは「bot」、パーミッションに「Manage Messages」を指定してください**
1. サーバの任意のテキストチャンネルから、翻訳したいテキストメッセージに対して絵文字でリアクションを打ちます
1. DM宛てにBOTから翻訳結果が返されます
    * その後、付与したリアクションは自動的に削除されます

## BOTとのDM間での使い方
1. botのDMに、翻訳したい文章をテキストメッセージで送信します
1. 送信したテキストメッセージに対して絵文字でリアクションを打ちます
1. DM内でBOTから翻訳結果が返されます

## 使用している主なライブラリなど

Discord.py<br>
https://discordpy.readthedocs.io/ja/latest/

Deepl API<br>
https://www.deepl.com/ja/docs-api