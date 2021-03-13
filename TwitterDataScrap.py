import twint
import asyncio
import nest_asyncio

nest_asyncio.apply()
c = twint.Config()
c.Search  = "snyderCut"
c.Limit = 10
c.Store_csv = True
c.Output = "../data/none.csv"
c.Lang = "en"
#c.Translate = True
#c.TranslateDest = "eng"
twint.run.Search(c)


loop = asyncio.get_event_loop()
loop.is_running()
