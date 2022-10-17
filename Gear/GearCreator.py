from Gear.Head import Head
from Gear.Bottom import Bottom
from Gear.Shoes import Shoes
from Gear.Shoulders import Shoulders
from Gear.Gloves import Gloves
from Gear.Top import Top


class GearCreator:

    def retrieveGear(self, type: str):
        head = Head(type)
        shoes = Shoes(type)
        shoulders = Shoulders(type)
        bottom = Bottom(type)
        gloves = Gloves(type)
        top = Top(type)

        if type == "Leather":
            return {
                "head":head.clone(type),
                "shoulders": shoulders.clone(type),
                "top": top.clone(type),
                "bottom": bottom.clone(type),
                "gloves": gloves.clone(type),
                "shoes": shoes.clone(type)
                }
        if type == "Mail":
            return {
                "head":head.clone(type),
                "shoulders": shoulders.clone(type),
                "top": top.clone(type),
                "bottom": bottom.clone(type),
                "gloves": gloves.clone(type),
                "shoes": shoes.clone(type)
                }
        if type == "Cloth":
            return {
                "head":head.clone(type),
                "shoulders": shoulders.clone(type),
                "top": top.clone(type),
                "bottom": bottom.clone(type),
                "gloves": gloves.clone(type),
                "shoes": shoes.clone(type)
                }
        if type == "Plates":
            return {
                "head":head.clone(type),
                "shoulders": shoulders.clone(type),
                "top": top.clone(type),
                "bottom": bottom.clone(type),
                "gloves": gloves.clone(type),
                "shoes": shoes.clone(type)
                }


gearCreator = GearCreator()