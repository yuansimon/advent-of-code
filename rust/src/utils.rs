use std::fmt;

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

#[derive(Clone, Debug)]
pub struct Range {
    left: i64,
    right: i64,
}

impl fmt::Display for Range {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "({}, {})", self.left, self.right)
    }
}

#[allow(dead_code)]
impl Range {
    pub fn format_vec(v: &Vec<Range>) -> String {
        format!("[{}]", v.iter().fold("".to_string(), |prefix, range|
            if prefix == "" {
                format!("{}", range)
            } else {
                format!("{prefix}, {}", range)
            })
        )
    }

    pub fn format_option(option: &Option<Range>) -> String {
        if let Some(ref range) = option {
            format!("{}", range)
        } else {
            "-".to_string()
        }
    }

    pub fn new(left: i64, right: i64) -> Result<Self, ()> {
        if left <= right {
            Ok(Range { left, right })
        } else {
            Err(())
        }
    }

    pub fn get_left(&self) -> i64 {
        self.left
    }

    pub fn get_right(&self) -> i64 {
        self.right
    }

    pub fn width(&self) -> u32 {
        (self.right - self.left) as u32
    }

    pub fn len(&self) -> u32 {
        (self.right - self.left + 1) as u32
    }

    pub fn translate(&self, offset: i64) -> Range {
        Range::new(self.left + offset, self.right + offset).unwrap()
    }

    pub fn intersect_other(&self, other: &Range) -> (Option<Range>, Option<Range>, Option<Range>) {
        let left_remains = if self.left < other.left {
            Some(Range::new(self.left, self.right.min(other.left - 1)).unwrap())
        } else {
            None
        };

        let intersect = Range::new(self.left.max(other.left), self.right.min(other.right)).ok();

        let right_remains = if other.right < self.right {
            Some(Range::new(self.left.max(other.right + 1), self.right).unwrap())
        } else {
            None
        };

        (left_remains, intersect, right_remains)
    }

    pub fn intersect(&self, other: &Range) -> Option<Range> {
        self.intersect_other(other).1.or_else(|| other.intersect_other(self).1)
    }

    pub fn intersect_ranges(&self, other: &Vec<Range>) -> Vec<Range> {
        let mut result: Vec<Range> = vec![];
        other.iter().for_each(|range| match self.intersect(&range) {
            Some(r) => result.push(Range::new(r.left, r.right).unwrap()),
            None => ()
        });
        result
    }

    pub fn contains(&self, point: i64) -> bool {
        self.left <= point && point <= self.right
    }
}
