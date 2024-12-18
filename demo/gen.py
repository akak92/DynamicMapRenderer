from mapnik import Map, load_map, render_to_file, Color

def draw_map() -> str:
    try:
        map = Map(734, 1036)  
        load_map(map, '/app/layout/stylesheet.xml')
        
        map.background = Color('white')
        
        map.zoom_all()

        render_to_file(map, '/app/results/demo_output.png')
    except Exception as exc:
        return f"an error occurred: {exc}"

    return "Map generated successfully!"

if __name__ == "__main__":
    demo_output: str = draw_map()
    print(demo_output)
