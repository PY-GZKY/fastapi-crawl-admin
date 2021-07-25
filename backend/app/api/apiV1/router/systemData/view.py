# -*- coding: utf-8 -*-
# @Time : 2020-12-13 19:48



from app.api.utils.responseCode import resp_200, resp_500



from fastapi import APIRouter
from starlette.requests import Request
import psutil

router = APIRouter()


def systemTestCharts(*, request: Request):
    try:
        result = {
            "systemTestCharts0": {
                "category": ["2020-12-19", "2020-12-20", "2020-12-21", "2020-12-22", "2020-12-23",
                             "2020-12-24",
                             "2020-12-25", "2020-12-26", "2020-12-27", "2020-12-28", "2020-12-29",
                             "2020-12-30",
                             "2020-12-31", "2021-1-1", "2021-1-2", "2021-1-3", "2021-1-4", "2021-1-5",
                             "2021-1-6",
                             "2021-1-7", "2021-1-8", "2021-1-9", "2021-1-10", "2021-1-11", "2021-1-12",
                             "2021-1-13",
                             "2021-1-14", "2021-1-15", "2021-1-16", "2021-1-17", "2021-1-18", "2021-1-19",
                             "2021-1-20",
                             "2021-1-21", "2021-1-22", "2021-1-23", "2021-1-24", "2021-1-25", "2021-1-26",
                             "2021-1-27",
                             "2021-1-28", "2021-1-29", "2021-1-30", "2021-1-31", "2021-2-1", "2021-2-2",
                             "2021-2-3",
                             "2021-2-4", "2021-2-5", "2021-2-6", "2021-2-7", "2021-2-8", "2021-2-9",
                             "2021-2-10",
                             "2021-2-11", "2021-2-12", "2021-2-13", "2021-2-14", "2021-2-15", "2021-2-16"],
                "lineData": [4.745368065767019, 166.18071554792425, 303.4510493110095, 213.1826005696548,
                             264.0121699874825,
                             118.05043002098569, 264.495613405586, 260.3929831444022, 206.09138101320656,
                             148.2272473050067,
                             150.32862485436857, 147.52039709680585, 110.41656889938012, 157.46386327037442,
                             203.49008668968347, 255.96018385156992, 215.86505251097248, 186.50110159853,
                             192.59489366027142, 115.61464930334057, 239.1996197004151, 235.80715643832264,
                             225.614476827134, 252.79745951359334, 174.5730360652415, 171.8987322204117,
                             226.07991263547018,
                             183.48869123808535, 175.57292604112882, 151.3742464816151, 186.5361552961991,
                             269.8321643614968, 255.36090951897137, 166.3067965283566, 78.78693236860333,
                             145.19704931839607, 229.9827840677091, 244.82096100202008, 218.92537442425726,
                             244.93434156887514, 134.24761908605825, 95.56140714601199, 100.10105771531768,
                             356.2774445267527, 316.11439118402967, 114.0049842070812, 146.73074745190755,
                             115.32937429047695, 191.80867241252622, 171.80079054127648, 156.18428773215513,
                             44.26143543007868, 262.25998791435563, 225.2474558802934, 212.0439880955767,
                             289.4362031755087,
                             165.8561444864526, 317.64956434171074, 139.80720650565752, 60.999046842634414],
                "barData": [3.1809544712145588, 115.24588070504281, 118.63794973277106, 75.32530084659376,
                            140.42809937404664, 39.17801675077204, 122.64215444828505, 87.11257641296454,
                            85.75508292193797,
                            54.98348936796913, 108.05024462429138, 76.22656503284229, 100.00268768654857,
                            84.52202988733247,
                            20.418814878017997, 136.4910452404838, 158.47343506288613, 8.91138396939688,
                            167.05203633005686,
                            54.34831836714626, 53.369958667954975, 90.42880183080241, 81.9091470438142,
                            143.04824846213205,
                            94.60380696374506, 148.7325580016536, 139.95878853688032, 26.83484547334669,
                            162.9724795260015,
                            100.88468208986785, 1.3482988084894565, 121.44995851244049, 183.33839887822236,
                            57.10210795929407, 69.72714919805685, 125.67686904418171, 183.42119035323233,
                            106.6062771871417,
                            72.78161996201517, 139.40099071185153, 26.193191575713115, 56.22272307478,
                            33.67932724695528,
                            167.77993821125165, 166.57733793722636, 9.39301013334144, 21.898522032039615,
                            0.8057000839270856, 19.38169155586933, 77.12303761434055, 23.998690134710987,
                            36.90530291934988,
                            153.88185704915537, 192.53401087515445, 110.321195665305, 147.5448537479482,
                            71.96443875755038,
                            163.27283278153342, 57.79140858141294, 12.59174804362364],
            },
            "systemTestCharts1": [{"value": 335, "name": "直接访问"},
                                  {"value": 310, "name": "邮件营销"},
                                  {"value": 234, "name": "联盟广告"},
                                  {"value": 135, "name": "视频广告"},
                                  {"value": 1548, "name": "搜索引擎"},
                                  ],
            "systemTestCharts2": [
                ["2019-10-10", 200],
                ["2019-10-11", 400],
                ["2019-10-12", 650],
                ["2019-10-13", 500],
                ["2019-10-14", 250],
                ["2019-10-15", 300],
                ["2019-10-16", 450],
                ["2019-10-17", 300],
                ["2019-10-18", 100],
            ]
        }

        return resp_200(data=result)
    except:
        return resp_500()


# ------------------------------- 路由添加 --------------------------------

router.add_api_route(methods=['GET'], path="/testCharts", endpoint=systemTestCharts)
