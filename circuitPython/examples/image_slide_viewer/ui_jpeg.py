import time
import bteve as eve_module

class ui_jpeg:
    def __init__(self, eve:eve_module.Brt_PicoEve_Module) -> None:
        self.eve=eve
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0
        self.index = 0
        self.image_num = 0
        self.images=[]
        self.names=[]
        pass
        
    def set_images(self, images, names):
        self.images=images
        self.names=names
        self.image_num=len(images)
        self.draw_1_image(images[self.index], self.names[self.index])

    def swipe_left(self):
        self.swipe_image('left')
        self.index+=1
        if self.index >= self.image_num:
            self.index=0
        self.draw_1_image(self.images[self.index], self.names[self.index])

    def swipe_right(self):
        self.swipe_image('right')
        self.index -=1
        if self.index < 0:
            self.index=self.image_num-1
            
        self.draw_1_image(self.images[self.index], self.names[self.index])

    def swipe_image(self, direc):
        eve=self.eve
        offset = 0
        
        x = self.x
        y = self.y
        w = self.w
        h = self.h
        name = self.name

        if direc=='right':
            direc=-1
        else:
            direc=1
        
        while offset < (x + w):
            eve.ClearColorRGB(255, 255, 255)
            eve.Clear()
            eve.ColorRGB(255, 255, 255)
            eve.VertexFormat(4)
            
            eve.Begin(eve.BITMAPS)
            eve.Vertex2f(x-offset*direc, y)

            tx = x - offset*direc + w/2 - len(name) * 5
            ty = y + h + 10

            eve.ColorRGB(0, 0, 0)
            eve.cmd_text(tx, ty, 30, 0, name)
            eve.swap()
            offset += 10 + offset/5
            time.sleep(0.01)

        eve.ClearColorRGB(255, 255, 255)
        eve.Clear()
        eve.ColorRGB(255, 255, 255)
        eve.swap()

    def draw_1_image(self,image, name):
        eve=self.eve
        eve.swap()

        eve.ClearColorRGB(255, 255, 255)
        eve.Clear()
        eve.ColorRGB(255, 255, 255)
        eve.VertexFormat(4)

        eve.cmd_loadimage(0, 0)
        eve.load(open(image, "rb"))
    
        eve.flush()
        rp=eve.EVE_Cmd_wp();
        eve.cmd_getprops(0, 0, 0)
        eve.flush()
        rp2=eve.EVE_Cmd_wp(); 
        ptr=eve.rd32(eve.RAM_CMD + rp+4*1);
        w=eve.rd32(eve.RAM_CMD + rp+4*2);
        h=eve.rd32(eve.RAM_CMD + rp+4*3);

        if w<0 or w > eve.w:
            w=500
        if h<0 or h > eve.h:
            h=500

        x=eve.w/2-w/2
        y=eve.h/2-h/2

        eve.Begin(eve.BITMAPS)
        eve.Vertex2f(x, y)

        tx = x + w/2 - len(name) * 5
        ty = y+ h + 10

        eve.ColorRGB(0, 0, 0)
        eve.cmd_text(tx, ty, 30, 0, name)
        eve.swap()
        eve.flush()

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.name = name
