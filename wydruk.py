from qgis.core import QgsProject
from qgis.gui import QgsMapCanvas

nazwa_kompozycji="mapka-du"

# Załaduj istniejącą kompozycję "mapa-du"
project = QgsProject.instance()
layout_manager = project.layoutManager()
layout = layout_manager.layoutByName(nazwa_kompozycji)

if layout:
    # Ustaw tryb Atlasu
    atlas = layout.atlas()
    atlas.setEnabled(True)  # Włącz atlas

    # Sprawdź, czy są jakieś obiekty w atlasie
    if atlas.featureCount() > 0:
        # Ustaw pierwszy obiekt atlasu jako aktywny
        atlas.setCurrentFeature(atlas.firstFeatureId())

    # Otwórz podgląd wydruku
    iface.openLayoutDesigner(layout)
    
else:
    print("Nie znaleziono kompozycji o nazwie:", nazwa_kompozycji)
