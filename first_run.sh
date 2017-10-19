ROOT=$(cd $(dirname $0) && pwd)

cp $ROOT/conf/db.py.sample $ROOT/conf/db.py
echo "\n下のファイルにデータベースの設定をする"
echo $ROOT/conf/db.py

