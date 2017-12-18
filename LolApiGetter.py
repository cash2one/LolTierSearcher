import requests

class LolApiGetter:
    def __init__(self, key=""):
        self.headers = {"X-Riot-Token": key, "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4"}
        self.url_getSummonerByName = "https://kr.api.riotgames.com/lol/summoner/v3/summoners/by-name/"
        self.url_getActiveGame = "https://kr.api.riotgames.com/lol/spectator/v3/active-games/by-summoner/"
        self.url_getRank = "https://kr.api.riotgames.com/lol/league/v3/positions/by-summoner/"

    def setApiKey(self, key):
        self.headers["X-Riot-Token"] = key

    def getSummonerInfo(self, nickname):
        url = self.url_getSummonerByName + nickname
        res = requests.get(url, headers=self.headers)
        status_code = res.status_code
        if status_code != 200:
            return None
        data = res.json()
        return data  # id, accountId, name, profileIConId, revisionDate, summonerLevel

    def getSummonerIdByName(self, nickname):
        summoner = self.getSummonerInfo(nickname)
        return summoner['id']

    def getActiveGameInfo(self, summonerId):
        url = self.url_getActiveGame + str(summonerId)
        res = requests.get(url, headers=self.headers)
        status_code = res.status_code
        if status_code != 200:
            return None
        data = res.json()
        return data

    def getRankInfo(self, summonerId):
        url = self.url_getRank + str(summonerId)
        res = requests.get(url, headers=self.headers)
        status_code = res.status_code
        if status_code != 200:
            return None
        data = res.json()
        return data

    def getEnermySummonerTier(self, nickname, gameInfo):
        result = []
        players = gameInfo["participants"]
        myIndex = 0
        for i in range(len(players)): # 자기 자신의 진형 확인을 위해 필요함
            player = players[i]
            name = player["summonerName"]
            if name == nickname:
                myIndex = i
                break
        # myIndex가 5 미만이라면 적은 5~9
        # myIndex가 5 이상이라면 적은 0~4

        enermyIndex = 0
        if myIndex < 5:
            enermyIndex = 5
        for i in range(enermyIndex, enermyIndex+5):
            player = players[i]
            name = player["summonerName"]
            id = player["summonerId"]
            tier = ""
            tier_rank = ""
            rankInfo = self.getRankInfo(id)

            if len(rankInfo):
                rank_solo = None
                for rank in rankInfo:
                    if rank["queueType"] == 'RANKED_SOLO_5x5': # 솔랭일때만
                        rank_solo = rank
                        break

                tier = rank_solo["tier"]
                tier_rank = rank_solo["rank"]
            else:
                tier = "없음"
                tier_rank = ""

            info = {"name": name, "tier": tier, "rank": tier_rank}
            result.append(info)
        return result

