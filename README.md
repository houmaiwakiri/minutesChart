# minutesChart

## lambda環境用

### src配下パッケージ管理について
txtでパッケージとverを管理する。
#### 1. Docker のインストール

Docker のパッケージをアップデート

```bash
sudo dnf update -y
```

Docker のインストール

```bash
sudo dnf install docker
sudo dnf install curl --allowerasing
# 最新のバージョンを取得
LATEST_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
# ダウンロード
curl -SL "https://github.com/docker/compose/releases/download/${LATEST_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod 750 /usr/local/bin/docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $(whoami)
```

#### 2. ソース

```bash
git clone https://github.com/houmaiwakiri/minutesChart.git
```

#### 3. Docker コンテナの構築

Docker イメージのビルド(main.py が実行される)

```bash
cd minutesChart
docker-compose up --build
```

実行終了後、ホスト側のminutesChart/src配下にpackageがインストールされる。
下記手順を踏み、S3にアップロードし、lambdaのレイヤーに追加する。
