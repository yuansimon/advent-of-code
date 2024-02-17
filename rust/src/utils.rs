#[macro_export]
macro_rules! dprintln {
    ($debug:expr, $($arg:tt)*) => {
        if $debug {
            println!($($arg)*);
        }
    };
}

#[macro_export]
macro_rules! dprint {
    ($debug:expr, $($arg:tt)*) => {
        if $debug {
            print!($($arg)*);
        }
    };
}

pub fn print_hr(add_newline: bool) {
    println!("---------------------------------------------------------------");
    if add_newline { println!() };
}

pub struct Rectangle {
    pub bottom_left: (i32, i32),
    pub width: u32,
    pub height: u32,
}

impl Rectangle {
    fn contains_x_cord(&self, x: i32) -> bool {
        self.bottom_left.0 <= x && x <= self.bottom_left.0 + self.width as i32
    }
    fn contains_y_cord(&self, y: i32) -> bool {
        self.bottom_left.1 <= y && y <= self.bottom_left.1 + self.height as i32
    }
    pub fn intersects_rectangle(&self, other: &Rectangle) -> bool {
        ((self.contains_x_cord(other.bottom_left.0) || self.contains_x_cord(other.bottom_left.0 + other.width as i32))
            && (self.contains_y_cord(other.bottom_left.1) || self.contains_y_cord(other.bottom_left.1 + other.height as i32)))
            || ((other.contains_x_cord(self.bottom_left.0) || other.contains_x_cord(self.bottom_left.0 + self.width as i32))
            && (other.contains_y_cord(self.bottom_left.1) || other.contains_y_cord(self.bottom_left.1 + self.height as i32)))
    }
}
