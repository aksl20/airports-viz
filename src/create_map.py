import  pandas as pd
from pathlib import Path
import folium

def main():
    data_dir = Path("../data")
    airports_file = data_dir / "airports.csv"
    frq_file = data_dir / "airport-frequencies.csv"
    runways_file = data_dir / "runways.csv"
    navaids_file = data_dir / "navaids.csv"

    # Load data
    frq = pd.read_csv(frq_file)
    airports = pd.read_csv(airports_file)
    runways = pd.read_csv(runways_file)
    navaids = pd.read_csv(navaids_file)


    data = airports.merge(runways, left_on="ident", right_on="airport_ident")
    data["length_ft"] = data["length_ft"] * 0.3048000
    large_airports = data.loc[data.type == "large_airport"]

    m = folium.Map(location=[35.73950057718963, 139.71080201185157],zoom_start=4, tiles='openstreetmap')

    folium.TileLayer(tiles="https://{s}.tile.jawg.io/jawg-sunny/{z}/{x}/{y}{r}.png?access-token=eEiMQqC52THxEEJwmODP3BtPzwB85n6wuIV85wRzlcF7D0hy0efXpK06TL8679V2", attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', name='Theme light').add_to(m)
    folium.TileLayer(tiles='https://{s}.tile.jawg.io/jawg-terrain/{z}/{x}/{y}{r}.png?access-token=eEiMQqC52THxEEJwmODP3BtPzwB85n6wuIV85wRzlcF7D0hy0efXpK06TL8679V2', attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', name='Theme Terrain').add_to(m)
    folium.TileLayer(tiles='https://{s}.tile.jawg.io/jawg-dark/{z}/{x}/{y}{r}.png?access-token=eEiMQqC52THxEEJwmODP3BtPzwB85n6wuIV85wRzlcF7D0hy0efXpK06TL8679V2', attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', name='Dark Theme').add_to(m)
    folium.TileLayer(tiles='https://{s}.tile.jawg.io/jawg-streets/{z}/{x}/{y}{r}.png?access-token=eEiMQqC52THxEEJwmODP3BtPzwB85n6wuIV85wRzlcF7D0hy0efXpK06TL8679V2', attr='<a href="http://jawg.io" title="Tiles Courtesy of Jawg Maps" target="_blank">&copy; <b>Jawg</b>Maps</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors', name='Street Theme').add_to(m)

    folium.LayerControl().add_to(m)

    for idx, airport in large_airports.iterrows():
        lat = airport.latitude_deg
        long = airport.longitude_deg
        folium.Marker(location=[lat, long], popup=f"<strong>{airport['name']}</strong>", tooltip=f"<strong>{airport['length_ft']}</strong>", icon=folium.Icon(icon='plane')).add_to(m)

    m.save("map.html")


if __name__ == "__main__":
    main()
