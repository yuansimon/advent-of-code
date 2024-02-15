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