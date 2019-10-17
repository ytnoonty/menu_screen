
import pymysql
import dbconfig
connection = pymysql.connect(host='localhost',
                             user=dbconfig.db_user,
                             passwd=dbconfig.db_password)

try:
    with connection.cursor() as cursor:

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Cider Donut','Hard Cider','7','','1911 Distillery','Lafayette, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Honeycrisp','Apple Wine','7','','1911 Distillery','Lafayette, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Population Pale Ale','Pale Ale','4.7','','Three Heads Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('The Kind','IPA','6.8','','Three Heads Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Wrought Iron IPA','American IPA','6.9','80','Abita Beer Co.','New Orleans, LA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hugh Malone','Belgian IPA','7.8','','Allagash Brewing Company','Maine ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('American Brown','Brown Ale','5','','Naked Dove','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Summer Solstice','Cream ale','5','','','Anderson Valley, CA ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Apricot Wheat','Fruit Wheat','4.9','','Ithaca Beer Co.','Ithaca NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bonito','Blonde Ale','4.5','','Ballast Point','San Diego, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Grapefruit Sculpin','IPA','7','','Ballast Point','CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Mango Even Keel','Session IPA with Mango','3.8','','Ballast Point','San Diego, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Red Velvet','Nitro Oatmeal Stout','5.5','','Ballast Point','San Diego, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Grapefruit Sculpin IPA','American IPA','7','','Ballast Point Brewing Company','California','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Barrier Evil Giant','American Rye IPA','6.5','','Barrier Brewing Co','Oceanside, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bass','English Pale Ale','5','','Bass Brewers Limited','United Kingdom (England)','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Beaver Bite IPA','American IPA','6.5','','Paradox Brewery','Schroon Lake, Adirondacks, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Beaver Overbite IPA','Northeast Style IPA','6','','Paradox Brewery','Schroon Lake,NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Oberon Ale','Wheat Ale','5.8','','Comstock Brewery','Comstock, MI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bells Porter','American Porter','5.6','','Comstock Brewery','Comstock, MI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bells Smitten','Rye Beer','6','','Comstock Brewery','Comstock, MI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Berry Naked Black Raspberry Ale','Fruit Beer','4.2','15','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hayburner IPA','IPA','7','','Big Ditch','Buffalo NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Billy Half Stack IPA','American IPA','6.6','','','Queens, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Blue Moon','Witbier','5.4','','Coors Brewing Company','Golden, Colorado','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Flower City Blonde Cider','Hard Cider','5','','Blue Toad Brewery','Henrietta, NY ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Briglin Road Red','Barrel Aged Red Ale','5.5','','Keuka Brewing Co.','Hammondsport NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Defender IPA','American IPA','5.9','','Brooklyn Brewery','Brooklyn, NY','','Heroically hopped golden IPA with strong notes of tropical fruit and dry finish.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Brooklyn Lager','American Amber Lager','5.2','','Brooklyn Brewing Co.','Brooklyn, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Brooklyn Pumpkin','','5','','Brooklyn Brewery','Brooklyn, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Brooklyn Summer Ale','Sunny Pale Ale','5','','Brooklyn Brewing Co.','Brooklyn, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Caged Alpha Monkey','American IPA','6.5','','Custom Brew Crafters','Honeyoye Falls, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Circus Boy The Hefeweizen','American Pale Wheat Ale','4.5','','Magic Hat Brewery','Vermont','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Clarity in the FLX IPA','American IPA','6.7','70','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Galactica IPA','American Double / Imperial IPA','8','','Clown Shoes','Ipswich, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Space Cake','American Double / Imperial IPA','9','','Clown Shoes','Ipswich, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Crimson Pistil IPA','American IPA','6.5','','Troegs Brewing Company','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('American Beauty','American Strong Ale','9','','Dogfish Head ','Milton, Deleware','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dogfish Head Beer For Breakfast','Milk/Sweet Stout','7.4','','Dogfish Head Craft Brewery','Milton, Deleware','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dundee Irish Red Lager','American Amber / Red Lager','5','','Genesee Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Empire Brewing Co. Ottos Amber Ale','American Amber / Red Ale','5.5','','Empire Brewing Co.','Syracuse, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Evil Giant IPA','IPA','6.3','','Barrier Brewing Co.','Oceanside, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Fat Tire','American Amber/Red Ale','4.2','','New Belgium Brewery','Colorado','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Fortem IPA','Unfiltered Imperial IPA','8.2','','Firestone Walker Brewing Co,','Paso Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Leo V. Ursus','American Imperial IPA','8.2','','Firestone Walker Brewing Co.','CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Luponic Distortion','American IPA','5.9','','Firestone Walker Brewing Co.','CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Easy Jack','IPA','4.5','','Firestone Walker Brewing Co.','Pass Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Union Jack ','American IPA','7','60','Firestone Walker Brewing Co.','Paso Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Firestone Walker Wookie Jack','American Black Ale','8.3','','Firestone Walker Brewing Co.','Paso Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Flying Dog Blood Orange IPA','Blood Orange IPA','','','','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Full Sail Amber','American Amber / Red Ale','5.5','','Full Sail Brewery','Oregon','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Galaxy IPA','American IPA','7.5','','Big Muddy Brewing','Illinois','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Black IPA','Black IPA','8','','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Blonde Ale','Blonde Ale - Pilot Batch Series','6','','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Double Bock','Double Bock - Pilot Batch Series','6.5','','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Helles Bock Lager','Lager','7','','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Light','Light Lager','3.6','','Genesee Brewery','Rochester, NY','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Oktoberfest','Golden Lager','5.5','20','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Orange Honey Cream Ale','Orange Honey Cream Ale','4.7','','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Scotch Ale','Scotch Ale','7.5','20','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genessee Oktoberfest','Golden Lager','5.5','20','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Goose Island IPA','English IPA','5.9','55','Goose Island Beer Co.','Chicago, Il','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Conways Irish Ale','Irish Ale','','','Great Lakes Brewing Co','Cleveland, Ohio ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Good Nature American Brown','Brown Ale','6.2','','Good Nature Farm Brewery Hamilton, NY','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Lakes Lake Erie Monster','American Double / Imperial IPA','9.1','','Great Lakes Brewing Co','Cleveland, Ohio ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Lakes Rally Drum Red Ale','Red Ale','5.8','','Great Lakes Brewing Co.','Cleveland, Ohio','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Lakes Steady Rollin Session IPA','Session IPA','4.8','','Great Lakes Brewing Co','Cleveland, Ohio ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Guinness','Stout - Irish Dry','4.2','45','Guinness','Ireland ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Guinness Blonde','American Pale Lager','5','','Guinness Ltd.','Ireland','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hamburg Octoberfest','Marzen / Oktoberfest','5.7','','Hamburg','Hamburg, NY ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Harp Lager','Euro Pale Lager','5','','Guinness Ltd.','Ireland','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Camp Wannamango','American Pale Ale with passion fruit and mango','5','','Harpoon Brewery','Boston, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hoponius Union','American Pale Ale','6.7','65','Jacks Abby Brewing','MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ithaca Casca Zilla','Red Ale','7','','Ithaca Brewing Co','Ithaca, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ithaca Daydreamer','Kolsh (German Style)','7','','Ithaca Brewing Co','Ithaca, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ithaca Flower Power','American IPA','7.5','','Ithaca Brewing Co.','Ithaca, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ithaca Hopkist Citrus IPA','Citrus IPA','4.8','','Ithaca Beer Company','Ithaca NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Keegan Ales Mothers Milk','Milk Sweet Stout','6','','Keegan Ales','Kingston, NY','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Labatt Blue Light Grapefruit','Pilsner with grapefruit ','4.0','','Labatt','Rochester, NY','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Labatt Summer Shandy','Lager with a splash of lemon','4','','Labatt','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Left Hand Wake Up Dead','Russian Imperial Stout','10.2','','Left Hand Brewing Co.','Colorado','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Leinenkugel Harvest Patch Shandy','Pumpkin Shandy','4.2','','Jacob Leinenkugel Brewing Co.','Chippewa Falls, WI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Summer Shandy','Weiss beer with lemonade flavor','4.2','','Jacob Leinenkugel Brewing Co.','Chippewa Falls, WI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Little Juice Coupe','Hoppy Lager','6.3','','Three Heads Brewing','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lost Borough 007 Undercover IPA','American IPA','7','','','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('# 9','Apricot Wheat ','5.1','20','Magic Hat Brewing Co.','South Berlington, VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Magic Hat Big Hundo IPA','IPA','9','','Magic Hat Brewery','Vermont','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Magic Hat Feast of Fools','Raspberry Stout','7.2','28','Magic Hat Brewing Company','Vermont','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Magic Hat Hefeweizen','American Pale Wheat Ale','4.5','','Magic Hat Brewery','Vermont','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Matts Burning Rosids','Saison / Farmhouse Ale','10.5','','Stone Brewing Co.','California','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Miller Lite','Lager','4.2','10','Miller Brewing Company','Milwaukee, Wisconsin','','','Bottle')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove NacktHopfen','German Hopped Pale Ale ','5.2','','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove Oktoberfest','Marzen','6.5','25','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove Session Pale Ale','American Pale Ale','4.5','','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove Wind Blown Amber Ale','American Amber','5','','Naked Dove Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ommegang Nirvana IPA','American IPA','6.5','','','Cooperstown, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Otter Creak Free Flow IPA','American IPA','6','','','Middlebury, VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Peak Organic Super Fresh','Dry Hopped Pilsner','7.6','','Peak Organic Brewing Co.','Maine','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Peak Organic Super Fresh','Hopped Pilsner','7.6','','Peak Organic Brewing Co.','Maine','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Pinner Throwback IPA','American IPA','4.9','','Oskar Blues Brewery','Longmont, CO','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ransack The Universe IPA','American IPA','6.8','','Collective Arts Brewery','Ontario, Canada','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bad Ass IPA','American IPA','6','','ROC Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dark and Mild','English Mild Ale','4','15','ROC Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Mocha Caramel Porter','Porter','5.5','','ROC Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('ROC Sassy Pants','Saison / Farmhouse Ale','6.2','','ROC Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Oktoberfest','German Style','5.9','17','Rohrbach Brewing Co.','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Railroad Street IPA','American IPA','6.5','66','Rohrbach Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Red Wing Ale','American Amber Ale','4.6','13','Rohrbach Brewing Co.','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Scotch Ale','Scottish-style Ale','6.8','16','Rohrbach Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Cookies & Milk Stout','Milk Stout','7.4','20','Rohrbach Brewing Co.','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Space Kitty IPA','American Double IPA','8.4','96','Rohrbach Brewing Co.','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Matt`s Brown Ale','American Brown Ale','4.3','13','Rohrbach Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Roktoberfest','German Lager','6','21','Three Heads Brewing','Rochester, NY','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sam Adams Summer Ale','American Wheat Ale','5.3','7','Sam Adams','Boston, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Saranac Octoberfest','German Lager','5.4','20','F.I. Matt Brewing Co.','Utica, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Saranac Big Moose Ale','American Pale Ale','5.3','','Matt Brewing Company','Utica, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Shipyard Pumpkinhead Ale','Pumpkin Wheat Ale','4.5','','Shipyard Brewing Co.','Portland, ME','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sierra Nevada Beer Camp','Czech Pilsener','5.2','','Sierra Nevada Brewing Co.','\\California ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sierra Nevada Hop Hunter IPA','American IPA','6.2','','','California','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Single Cut Billy Half Stack IPA','IPA','6.6','88','Singlecut Beersmiths','Queens, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Single Cut Dean Pacific Northcoast Mohogany','Red Ale','6','','','Queens, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Smithwicks','Irish Red Ale','4.5','','Guinness Ltd','Ireland','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Smutty Clustards Last Stand','American IPA','8.3','','Smutty Nose Brewing Co.','New Hampshire','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Smutty Nose Pumpkin Ale','Pumpkin Ale','5.8','','Smutty Nose Brewing Co.','New Hampshire','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Pumking','Pumpkin Ale','8.6','','Southern Tier','Lakewood, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sierra Nevada Hop Bullet','Double IPA','8','60','Sierra Nevada Brewing Co. Chico, CA','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stella Artois Cidre','Saison/Farmhouse Cider','4.5','','','Belgium','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stone IPA','IPA','6.9','71','Stone Brewing','San Diego, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stone Mixtape IPA','IPA','6.4','','Stone Brewing Co.','Escondito, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Back Porch Cream Ale','Cream Ale','5.5','','Stoneyard Brewing Co.','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Hazy Hoppy Nonsense','IPA','6','','Stoneyard Brewing','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Rye-It','Imperial Porter','8','','Stoneyard Brewing Co.','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Swiftwater IPA','American IPA','7','','Swiftwater Brewing','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Three Heads Brewing Mandarillo Pale Ale','Pale Ale','5','38','Three Heads Brewing','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Troegs Crimson Pistil IPA','American IPA','6.5','','Troegs Brewing Company','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Troegs Nitro Chocolate Stout','Stout','7.1','','Troegs Brewing Co.','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Nugget Nectar','Imperial Double Red Ale','7.5','93','Troegs Independent Brewing','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Summer Love','Golden Ale','5.2','25','Victory Brewing Co','Downingtown, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Voodoo Ranger IPA','IPA','7','','New Belgium Brewing Co.','Fort Collins, Co','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Wachusett Blueberry Ale','','4.5','','','MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Windblown Amber Ale','American Amber Ale','5','25','Naked Dove Brewing Co','Canadigua, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Woodcock Bros. Hoppy Cock','American IPA','6','','Woodcock Bros Brewing Co.','Wilson, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Yuengling Traditional Lager','Lager - American Amber / Red','4.5','16','Yuengling Brewery','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Fighting Irish Ale','IPA','7','','','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stella Artois','European Lager','5','24','Stella Artois Brewery','Vlaams-Brabant Belgium','','','Draft & Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Thirsty Dog Old Leghumper ','American Porter','5.8','24','Thirsty Dog Brewing Company ','Akron, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dogfish Head Liquid Truth','IPA','6.8','65','Dogfish Head Brewery','Milton, Deleware','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove Naughty & Nice ','Winter Warmer','6','15','Naked Dove Brewing Co.','Canandaigua, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Two Hearted Ale','American IPA','7','55','Bells Brewery','Comstock, MI','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Cloudbank ','Hefeweizen','5','13','Wagner Valley','Lodi, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Troegs Mad Elf','Dark Ale','11','15','Troegs Brewing Co.','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Dark Chocolate Scotch Ale','Scotch Ale','7.5','20','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee IPA','IPA','7','70','Genesee Brewery ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Coffee Stout','Stout','5','36','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbach Kaseys Kristmas Ale','Winter Ale','5','','Rohrbach Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Southern Tier IPA','American IPA','7','60','Southern Tier Brewing Co.','Lakewood, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Smuttynose Robust Porter','American Porter','6.2','61','Smuttynose Brewing Co.','Hampton, NH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ellicottville Ski Bum','Hopped Winter Ale','6','25','Ellicottville Brewing Co.','Ellicottville, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Red Nutz!','American Amber/Red Ale','6.4','24','Roc Brewing Co. ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Single Cut 18 Watt IPA','American IPA','5','','Singlecut Beersmiths','Queens, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Southern Tier Old Man Winter','American IPA','6','55','Three Heads Brewing Rochester NY','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('60 Minute IPA','American IPA','6','60','Dogfish Head ','Milton, DE','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Red Nutz','Red/Amber Ale','6.4','24','Roc Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Magic Hat TFG IPA','American IPA','6.6','66','Magic Hat Brewing Co.','South Berlington, VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Bock','Bock','5.2','','Genesee Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Voodoo Ranger Juicy Haze ','New England IPA','7.5','50','New Belgium Brewing Company','Fort Collins, CO','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Little Sumpin Sumpin Ale','Pale Ale - Wheat','7.5','65','Lagunitas Brewing Company','Petaluma, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lost Borough Cream Ale','Cream Ale','5.2','17','The Lost Borough Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Conways Irish Ale','Irish Ale','6.3','26','Great Lakes Brewing Co.','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Paradox Overbite ','','','','','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Kilkenny Irish Cream Ale','Cream Ale','4.3','','Guinness Brewery','Dublin, Ireland','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Southern Tier Nu Skool IPA','IPA - American','6','55','Southern Tier Brewing Co',' Lakewood, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Triphammer IPA','American IPA','6.8','','Triphammer Bierwerks','Fairport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Triphammer Rye Pale Ale','Rye Ale','5','45','Triphammer Bierwerks','Fairport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Young Lion IPA','IPA','6.5','57','Young Lion Brewing Co.','Canandaigua, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dreamweaver','Hefeweizen','4.8','15','Troegs Independent Brewing','Hershey, PA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Honey Kolsch','Kolsch','4.8','26','Keuka Berwing Co.','Hammondsport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Labatt Blue','Pilsner','5','12','Labatt','Toronto, ON','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Magners Original Irish Cider','Cider','4.5','','Magners Irish Cidery','Clonmel, Co. Tipperary, Ireland','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Pilot Batch S.M.A.S.H. Pale Ale','Pale Ale','6','56','Genesee Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Grand Master Dunk','Lager-Dunkel Munich','5.8','22','Rohrbach Brewing Company','Rohrbach Micro Brewery','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Blueberry Wheat Ale','Fruit Ale','4.8','11','Ellicottville Brewing Company','Ellicottville, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Pilsner Urquell','Pilsner-Czech','4.4','40','Plzensky Prazdroj','Czesch Republic','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Ruby Red Kolsch','Kolsch','4.5','8','Genesee Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Tropical Storm IPA','New England Style IPA','6','50','Saranac Brewery ','Utica, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Red Wing Ale','American Amber Ale','4.6','13','Rohrbach Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hazy Little Thing','New England Style IPA','6.7','40','Sierra Nevada Brewing Co.','Chico, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Weird and Gilly','New England Style IPA','6.6','88','Singlecut Beersmiths','Astoria, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Blue Moon Mango','Fruit Wheat Beer','5.4','33','Blue Moon Brewing Co.','Denver, CO','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Tropical Storm','IPA','6','50','Saranac ','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Boom Sauce','IPA','7.8','78','Lord Hobo Brewing Co.','Woburn, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('One Off Ale','Double IPA','9.2','88','Naked Dove Brewing Company','Canandaigua. NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Fathom IPA ','American IPA','6','50','Bastast Point Brewing Company','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Whoopass Double IPA','Double IPA','8','77','ROC Brewing Company','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Angry Orchard Rose','Cider','5.5','','Angry Orchard','Cincinatti, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Modelo Especial','Lager','4.5','18','Grupo Modelo ','Mexico City, D.F. Mexico','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Blueberry Ale','Fruit Beer','4.5','14','Rohrbach','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Mosaic Cream Ale','Dry Hopped Cream Ale','6.4','16','Genesee Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Griddle Cakes','Pale Wheat Ale','5.2','','Rohrbach Brewing Co','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Tart Peach Kolsch','Kolsch','5.2','','Ballast Point Brewing Co','San Diego CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Elder Betty','Elderberry Pale Wheat Ale','5.5','13','Magic Hat','Burlington, VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Barroom Hero','English Pub Ale','4.2','15','Magic Hat Brewing Company','Burlington, VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Point The Way IPA','Session IPA','5.5','60','Golden Road Brewing','Los Angeles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lagunitas Sumpin Easy ','Pale Ale','5.7','51','Lagunitas Brewing Company','Petaluma, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('DIPA','Pale ale ','9.2','','Naked Dove Brewing Company','Canandaigua, NY ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Alpaca Kisses','IPA','6.5','','Swiftwater Brewing Company','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('UFO White Ale','Witbier','4.8','11','Harpoon Brewery','Boston, MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Orange Honey Cream Ale','Cream Ale','4.7','','Genesee Brewing','Rochester','Http://www.genesee.com','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sip of Sunshine','Dbl IPA','8','65','Lawsons Brewery','Wareen VT','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Harpoon IPA','IPA','5.9','42','Harpoon Brewery','Boston MA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Southern Pecan Brown Ale','Nut Brown Ale','4.5','19','Lazy Magnolia','Kiln, MS','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Aloha Sculpin','American IPA','7','70','Ballast Point Brewing Co.','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sam `76','American Light Lager','4.7','12','Boston Beer Company','Boston, MA','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Angelica','American Pale Wheat Ale','5.5','','Lord Hobo','Massachusetts','http://www.lordhobobrewing.com','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Strictly Hand-Held Honey Kolsch','Kolsch','5.0','','SingleCut Beersmiths','New York','SingleCutbeer.com','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Holy Moses Rasperry White Ale','Witbier','6.2','','Great Lakes','Ohio, United States','greatlakesbrewing.com','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('C Hops','American Pale Ale','5.5','','Firestone Walker','California ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Jai Alai IPA','American Style IPA','7.5','70','Cigar City Brewing','Tampa, FL','','American Style IPA','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Burning Money ','New England Style IPA','6.6','80','Thin Man Brewery','Buffalo, NY','','Citrus, melon, soft bitterness ','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Glorious','New England Style Pale Ale','6.5%','72','Lord Hobo','Massachusetts ','','Beautifully Smooth anew England Style Pale Ale. Pours a hazy straw color. A double dose of much sought after Galaxy hops gives of a silky peach-mango-grape aroma, tropical fruit flavors, and elegantly soft mouth feel. ','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lagunitas IPA','American IPA','6.2','52','Lagunitas Brewing Co.','Petaluma, CA','Lagunitas.com','Classic American IPA. ','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Guayabera ','Citra Pale ale','5.5','42','Cigar city','Tampa bay, Florida ','Cigar city brewing.com','American Pale ale','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Vermont IPA','VT IPA','6.0%','45','Long Trail','Bridgewater, VT','www.longtrail.com','Hazy New England IPA w/ big notes of citrus, pineapple, and tropical fruit.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Guayabera','Pale Ale','5.5','50','Cigar City Brewing','Tampa, FL','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Strong Arm','New England Style IPA','6','60','Three Heads Brewery ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hoppy Pils','Pilsner','4.7','','Genesee','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Petal Pusher','Session IPA','4.25','','Ithaca','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Petal Pusher','Session IPA','4.25','','Ithaca Beer Company','Ithaca, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('!1 Ticker News Headline','','','','','','','St. Patrick`s day. ..... Slainte','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Vt IPA','IPA','6.00','','Long Trail Brewing ','Vermont ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dortmunder Gold','Lager','5.8','30','Great Lakes Brewing Co.','Cleveland, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dortmunder Gold','Lager','5.8','30','Great Lakes Brewing Co.','Cleveland, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Good Nature','American Brown Ale','6.2','','Good Nature Brewing ','Hamilton, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Nu Skool IPA','IPA','6','','Southern Tier','New York','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bud Light','Lager','4.2','27','Anheuser-Bush','St. Louis','','','Both')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Conehead','IPA','5.7','','Zero Gravity ','Burlington VT','','All Citra hopped IPA','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Copper Legend ','Oktoberfest ','5.7','22','Jack`s Abby','Massachusetts ','','Malty, smooth and exceedingly drinkable','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Brett`s Milkshake IPA','Passion Fruit IPA','6.8','','Sierra Nevada ','Asheville, NC','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Uniduckdapuss','Sour - Fruited Raspberry IPA','6.5','65','Triphammer Bierwerks','Fairport','Www.triphammerbierwerks.com','Rare animal of western New York- enjoys red fruit, loves climbing bines and likes to pucker. Observed and recorded by Cleo. Made in commemoration in September. It`s a kettle sour, more tart than sour. ','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Tears of Green IPA','IPA','7.5','','Captain Lawrence','Elmsford, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Coors Light','','','','','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Budweiser','Lager','5','12','Anheuser-Bush','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Michelob ULTRA','Lager - American Light','4.2','10','Anheuser-Busch','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Samuel Adams Boston Lager','Lager - Vienna','5','30','Boston Beer Company','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Heineken','Lager - Euro','5','19','Heineken','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Heineken Light','Lager - American Light','3.3','12','Heineken','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Modelo Especial','Lager','4.5','18','Grupo Modelo','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Labatt Blue Light Lime','Lager - American Light','4','','Labatt Brewing Company','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bud Light Orange','Lager - American Light','4.2','','Anheuser-Busch','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Woodchuck Amber Hard Cider','Cider','5','','Woodchuck Cidery','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Angry Orchard Crisp Apple','Cider - Sweet','5','10','Angry Orchard Cider Company','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('1911 Hard Cider','Cider','5.5','','Beak & Skiff Apple Orchards','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Kaliber','Non-Alcoholic Beer','0','0','Guinness','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Labatt Blue N/A','Non-Alcoholic Beer','.5','','Labatt Brewing Company','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('3HB Lager','Lager','5','18','Three Heads Brewing','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Hell or High Watermelon','Fruit Beer','4.9','17','21st Amendment Brewery','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Beer','Lager','4.5','20','Genesee Brewing Co','Rochester, NY','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Cream Ale','Cream Ale','5.2','','Genesee Brewing Co','Rochester, NY','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Coors Banquet','Lager','5','15','Coors Brewing Co','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bud Light Lime','Lager - American Light','4.2','8','Anheuser-Busch','','','','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('FC For Our City','IPA - Session / India Session Ale','4.1','21','Big Ditch Brewing Co','Buffalo, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Belgian White','Witbier','5.2','','Shock Top Brewing Co.','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Copper Legend Octoberfest','Marzen','5.7','22','Jack`s Abby Craft Lagers','','','','Draft')"""
        cursor.execute(sql)


        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Alpenglow','Red IPA','6.5','65','Rohrbach Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee 12 Horse ','Ale','5.10','','Genesee Brewery ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Brett`s Milkshake IPA','Milkshake IPA','6.6','40','Sierra Nevada','Chico, CA','','Fruity IPA','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Firestone Walker Lager','German Helles','4.5','','Firestone Walker','Paso Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Octoberfest','','','','','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Young Lion Octoberfest','Marzen ','6.3','','Young Lion','Canandaigua, NY','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('1911 Raspberry Cider','Cider - Other','5.5','0','Beak & Skiff Apple Orchards','Lafayette, NY, United States','http://www.1911spirits.com/ciders.html','1911 Raspberry Hard Cider is a sparkling cider made from our family grown apples. This cider opens with a fruit forward body and a lingering burst of raspberry on the finish. Semi-Sweet.','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Too Kind','IPA - Imperial / Double','8.5','87','Three Heads Brewing','Rochester, NY, United States','http://www.threeheadsbrewing.com','Our mamas always taught us that you can never be too polite. In their honor, we decided to test that theory with the Too Kind. It has everything you love from the Kind IPA but jacked up to an out-of-this-world level. A hop exuberance of pine, citrus and love that plays nice with others.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Space Kitty','IPA - Imperial / Double','8.4','96','Rohrbach Brewing Company','Rochester, NY, United States','http://www.rohrbachs.com','This American Double IPA features a trio of rare hops, high in alpha acids and juicy oils, that mimic those wonderful IPAs and Double IPAs of the West Coast that we love so dearly. Do not age Space Kitty and please drink fresh!','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Space Rock','Pale Ale - American','5','72','Short`s Brewing Company','Bellaire, MI, United States','http://www.shortsbrewing.com/','A light bodied American Pale Ale with prominent floral and orange peel-like hop aromas. Only the slightest grainy malt qualities are detectable, as assertive bitter flavors of citrus rind and dandelion leaf take hold. The finish lingers with a waning bitterness that`s not overly dry.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Patrick Hayze','IPA','6.5','','Firestone Walker Brewing Co.','Los Robles, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Nosferatu','Imperial Red Ale','8.0','','Great Lakes Brewing Co.','Cleveland, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Mikkeller Windy Hill IPA','New England style IPA','7.0','','Mikkeller Brewing Co. ','Denmark/San Diego, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Founders All Day IPA','Session IPA','4.7','','Founders Brewing Co.','Michigan','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Dunkin Coffee Porter','Porter','6.00','28','Harpoon','Boston Ma.','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Belgian White','Witbier','5.4','9','Blue Moon Brewing Company','Denver, CO, United States','http://www.bluemoonbrewingcompany.com/','Blue Moon Belgian White, Belgian-style wheat ale, is a refreshing, medium-bodied, unfiltered Belgian-style wheat ale spiced with fresh coriander and orange peel for a uniquely complex taste and an uncommonly smooth finish.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Young Lion Super Dry','Lager - Japanese rice','6.0','','Young Lion Brewing Co.','Canandaigua, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Founders Dirty Bastard ','Scotch Ale','8.5','50','Founders Brewing Co.','Michigan','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Spring House Deep Grusome','American Stout','8.0','','Spring House Brewing Co.','Pennsylvania ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naked Dove Helles Lager','German Munich Helles','5.5','','Naked Dove Brewing Co.','Canandaigua, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee 12 Horse Ale','Blonde Ale','5.1','0','Genesee Brewing Company','Rochester, NY, United States','http://www.geneseebeer.com','Just re-introduced to the market again. October 2011','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Corona Extra','Lager - North American Adjunct','4.5','19','Grupo Modelo','Mexico City, Distrito Federal, Mexico','http://www.gmodelo.mx','Outside Mexico, Corona is often served with a wedge of citrus fruit - usually lime, occasionally lemon - inserted into the neck of the bottle. Within Mexico, especially in the south, Corona served with lime is not uncommon, but is not considered mandatory. Includes Coronita, Coronita Extra, Corona Mega and Corona Familiar. If you are having either a Michelada or a Corona-rita, please do not create a unique new beer since beer cocktails are not allowed.','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Corona Light','Lager - American Light','4.1','18','Grupo Modelo','Mexico City, Distrito Federal, Mexico','http://www.gmodelo.mx','Outside Mexico, Corona is often served with a wedge of citrus fruit - usually lime, occasionally lemon - inserted into the neck of the bottle. Within Mexico, especially in the south, Corona served with lime is not uncommon, but is not considered mandatory.','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard EveryMan IPA','IPA','5.5','40','Stoneyard Brewing Co. ','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Miller High Life','Lager - North American Adjunct','4.6','7','Miller Brewing Company','Milwaukee, WI, United States','http://www.millercoors.com','Miller High Life, also known as the Champagne of Beers, is a quintessentially classic, American-style lager. To this day, Miller High Life continues to be faithfully brewed as a golden pilsner, utilizing light-stable galena hops from the Pacific Northwest and a select combination of malted barley.','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Windy Hill','IPA - New England','7','70','Mikkeller Brewing San Diego','San Diego, CA, United States','http://www.mikkellersd.com/','Hazy IPA','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Three Heads Loopy','Oatmeal Red Ale','6.6','64','Three Heads Brewery ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Miller High Life','Lager - North American Adjunct','4.6','7','Miller Brewing Company','Milwaukee, WI, United States','http://www.millercoors.com','Miller High Life, also known as the Champagne of Beers, is a quintessentially classic, American-style lager. To this day, Miller High Life continues to be faithfully brewed as a golden pilsner, utilizing light-stable galena hops from the Pacific Northwest and a select combination of malted barley.','Bottle')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Black Cherry Hard Seltzer','Hard Seltzer','5','0','White Claw','Chicago, IL, United States','https://www.whiteclaw.com/','Spiked Hard Seltzer','Can')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ruby Grapefruit Hard Seltzer','Hard Seltzer','5','0','White Claw','Chicago, IL, United States','https://www.whiteclaw.com/','','Can')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lime Hard Seltzer','Hard Seltzer','5','0','White Claw','Chicago, IL, United States','https://www.whiteclaw.com/','Spiked Hard Seltzer','Can')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Raspberry Hard Seltzer','Hard Seltzer','5','0','White Claw','Chicago, IL, United States','https://www.whiteclaw.com/','Spiked Hard Seltzer','Can')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Southern Tier Citra Hop Live ','Pale Ale','5.5','37','Southern Tier','Lakewood NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Young Lion New England IPA','IPA - New England','7.1','70','Young Lion Brewing Company','Canandaigua, NY, United States','http://www.younglionbrewing.com','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Spring House Big Gruesome','Imperial Stout ','8.3','','Spring House ','Pennsylvania ','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Lagunitas Brown Shugga','American Strong Ale','10.0','51.1','Lagunitas Brewing ','Petaluma, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Frank Zappa Wild Stache IPA','IPA','7.3','53','Sierra Nevada ','CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Industrial Arts Wrench','New England IPA','6.8','','Industrial Arts Brewery ','Hamilton, ON','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Shock Top','Belgian White','5.2','','Shock Top Brewing Co. ','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Young Lion Cachorro de Leon','Red Lager','4.7','','Young Lion Brewing Co.','Canandaguia, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Juicy IPA','American IPA','6.0','38','Genesee Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbachs Fiver Brown Ale','Brown Ale','5.0','24','Rohrbachs Brewery','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Sierra Nevada Celebration','IPA','6.5','','Sierra Nevada Brewing Co.','Chico, CA','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Juice Bomb','American IPA','6.5','','Sloop Brewing','Elizaville, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Christmas Ale','Winter Ale','7.5','30','Great Lakes Brewing Company','Cleveland, OH, United States','http://www.greatlakesbrewing.com/','A holiday ale brewed with honey and spiced with fresh ginger and cinnamon.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Lakes Christmas Ale','Winter Warmer','7.5','','Great Lakes Brewing Co.','Cleveland, OH','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Three Heads Hippy Holidays','Amber Lager','6.5','','Three Heads Brewing ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Three Heads Sprucifer','IPA','6.0','','Three Heads Brewing ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Everyman IPA','IPA - American','5.5','40','Stoneyard Brewing Company','Brockport, NY, United States','http://www.stoneyardbrewingcompany.com','A hoppy American IPA with the addition of orange and flaked oats.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Great Lakes Christmas ale','Winter Warmer','7.5','','GREAT lakes Brewing Co.','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Ithaca Bullseye Red','Red Ale','5.2','','Ithaca Brewing Co.','Ithaca, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Blue Citra','Lager - Pale','4.7','30','Labatt Brewing Company','Toronto, ON, Canada','http://www.labatt.com/','A hoppy session lager brewed with Citra and Mosaic hops for fresh, juicy aromas and flavors of tropical fruit. Crisp and easy drinking, it represents a new kind of refreshing.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Salted Caramey Chocolate Porter','Porter','6.5','','Genesee Brewery ','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Salted Caramel Chocolate Porter','Porter ','6.5','','Genesee Brewery ','Rochester NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Bender IPA','IPA - American','6.5','0','Stoneyard Brewing Company','Brockport, NY, United States','http://www.stoneyardbrewingcompany.com','Mosaic and Amarillo hops combine to create a citrus and tropical fruit forward, mildly bitter, cloudy IPA.','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Juicehead ','New England Style DIPA','8.9','','Stoneyard ','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('-New Beer Coming Soon-','','','','','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Strike That','American IPA ','6.5','','Stoneyard Brewing Co.','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('New Belguim Accumulation','White IPA','6.2','55','New Belgium Brewery','','','','Draft')"""
        cursor.execute(sql)

        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('20 Plato DDH IPA','Double IPA','8.6','26','Upstate Brewing Company','Elmira, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('What The Kids Want IPA','IPA','6.8','','Swiftwater Brewing Co.','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Genesee Schwarzbier','Dark Session Lager','5.4','','Genesee Brewing Company ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Gangstas Pearadise','Cider','5.7','','OSB Ciderworks','','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Make Me Wanna Stout','Coffee Cream Stout','5.2','','Big Ditch','Buffalo, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('TNT IPA','IPA','5.0','','Singlecut ','Clifton Park, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Rohrbachs OK Be Jelly','Raspberry Porter ','7.0','27','Rohrbachs Brewing Company ','Rochester, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Stoneyard Ellsworth','IPA','6.5','','Stoneyard ','Brockport, NY','','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Naughty To the Core','Cider - Herbed / Spiced / Hopped','0','0','Naked Dove Brewing Company','Canandaigua, NY, United States','http://www.nakeddovebrewing.com/','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('High Roller','Saison / Farmhouse Ale','5.3','0','Ithaca Beer Company','Ithaca, NY, United States','https://www.ithacabeer.com/','','Draft')"""
        cursor.execute(sql)
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Big Ditch Hayburber','American IPA','7.0','','Big Ditch Brewing Co.','Buffalo, NY','','','Draft')"""
        sql = """INSERT INTO myflaskapp.list_history (`name`,`style`,`abv`,`ibu`,`brewery`,`location`,`website`,`description`,`draft_bottle_selection`) VALUES ('Diamond Star Halo ','DDH IPA','6.6','','Singlecut','Astoria, NY ','','','Draft')"""

        cursor.execute(sql)
        connection.commit()

finally:
        connection.close()
