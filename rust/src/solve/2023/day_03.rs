use indoc::indoc;

use crate::dprint;
use crate::dprintln;
use crate::solve::{Solver, TestCaseProvider};
use crate::utils::Rectangle;

pub struct Solve;

impl Solver for Solve {
    fn get_year() -> u32 {
        2023
    }

    fn get_day() -> u32 {
        3
    }

    fn is_part_one_solved() -> bool {
        true
    }

    fn is_part_two_solved() -> bool {
        true
    }

    fn part_one(debug: bool, input: &str) -> String {
        let (numbers, symbols) = parse(debug, input);
        let (number_rects, symbol_rects) = get_rectangles(debug, numbers, symbols);

        let mut sum = 0u32;
        for (num, num_rect) in number_rects {
            if symbol_rects.iter().any(|(_, sym_rect)| num_rect.intersects_rectangle(sym_rect)) {
                dprintln!(debug, "Value {} intersects a symbol", num.value);
                sum += num.value;
            }
        }

        sum.to_string()
    }

    fn part_two(debug: bool, input: &str) -> String {
        let (numbers, symbols) = parse(debug, input);
        let (number_rects, symbol_rects) = get_rectangles(debug, numbers, symbols);

        let mut sum = 0u32;
        for (sym, sym_rect) in symbol_rects.iter().filter(|(s, _)| s.symbol == '*') {
            let intersects: Vec<&(Number, Rectangle)> = number_rects.iter().filter(|(_, num_rect)| num_rect.intersects_rectangle(&sym_rect)).collect();
            if intersects.len() == 2 {
                let ratio = intersects.iter().fold(1, |acc, (num, _)| acc * num.value);
                dprintln!(debug, "Symbol {}@({},{}) is a gear with ratio {}", sym.symbol, sym.x, sym.y, ratio);
                sum += ratio;
            }
        };
        sum.to_string()
    }
}

type XCord = u32;
type YCord = u32;

#[derive(Debug)]
struct Number {
    value: u32,
    x: XCord,
    y: YCord,
    len: u32,
}

#[derive(Debug)]
struct Symbol {
    symbol: char,
    x: XCord,
    y: YCord,
}

fn get_rectangles(debug: bool, numbers: Vec<Number>, symbols: Vec<Symbol>) -> (Vec<(Number, Rectangle)>, Vec<(Symbol, Rectangle)>) {
    let number_rects: Vec<(Number, Rectangle)> = numbers.into_iter().map(|number| {
        let rect = Rectangle { bottom_left: (number.x as i32, number.y as i32), width: number.len - 1, height: 0 };
        (number, rect)
    }).collect();

    let symbol_rects: Vec<(Symbol, Rectangle)> = symbols.into_iter().map(|symbol: Symbol| {
        let rect = Rectangle { bottom_left: (symbol.x as i32 - 1, symbol.y as i32 - 1), width: 2, height: 2 };
        (symbol, rect)
    }).collect();

    dprint!(debug, "Number Rects: ");
    number_rects.iter().for_each(|(n, r)| dprint!(debug, "{}@(({},{}),{},{}) ", n.value, r.bottom_left.0, r.bottom_left.1, r.width, r.height));
    dprintln!(debug, "");

    dprint!(debug, "Symbol Rects: ");
    symbol_rects.iter().for_each(|(s, r)| dprint!(debug, "{}@(({},{}),{},{}) ", s.symbol,r.bottom_left.0, r.bottom_left.1, r.width, r.height));
    dprintln!(debug, "");
    (number_rects, symbol_rects)
}

fn parse_line(debug: bool, line: &str, y: YCord, numbers: &mut Vec<Number>, symbols: &mut Vec<Symbol>) {
    fn save_number(debug: bool, numbers: &mut Vec<Number>, x: XCord, y: YCord, len: u32, value: u32) {
        let number = Number { x, y, len, value };
        dprint!(debug, "{value}@{x}; ");
        numbers.push(number);
    }

    let mut is_parsing_number = false;
    let mut parsed_num_val = 0;
    let mut parsed_num_len = 0;
    let mut parsed_num_start_x = 0;
    for (x, char) in line.chars().enumerate() {
        let x = x as XCord;
        if char.is_digit(10) {
            if !is_parsing_number {
                parsed_num_start_x = x
            }
            is_parsing_number = true;
            parsed_num_len += 1;
            parsed_num_val *= 10;
            parsed_num_val += char.to_digit(10).unwrap();
        } else {
            if is_parsing_number {
                save_number(debug, numbers, parsed_num_start_x, y, parsed_num_len, parsed_num_val)
            }
            is_parsing_number = false;
            parsed_num_len = 0;
            parsed_num_val = 0;
            match char {
                '.' => (),
                symbol => {
                    dprint!(debug, "{}@{}, ", symbol, x);
                    symbols.push(Symbol { symbol, x, y });
                }
            }
        }
    }
    if is_parsing_number {
        save_number(debug, numbers, parsed_num_start_x, y, parsed_num_len, parsed_num_val)
    }
}

fn parse(debug: bool, input: &str) -> (Vec<Number>, Vec<Symbol>) {
    let mut numbers: Vec<Number> = vec![];
    let mut symbols: Vec<Symbol> = vec![];
    for (y, line) in input.lines().enumerate() {
        let y = y as YCord;
        dprint!(debug, "Parsing line {y}: ");
        parse_line(debug, line, y, &mut numbers, &mut symbols);
        dprintln!(debug, "");
    }
    (numbers, symbols)
}

struct TestCases;

impl TestCaseProvider<Solve> for TestCases {
    fn get_part_one_example_input() -> &'static str {
        indoc! {"
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..
        "}
    }

    fn get_part_one_example_output() -> &'static str {
        "4361"
    }

    fn get_part_one_real_output() -> &'static str {
        "525181"
    }

    fn get_part_two_example_input() -> &'static str {
        indoc! {"
            467..114..
            ...*......
            ..35..633.
            ......#...
            617*......
            .....+.58.
            ..592.....
            ......755.
            ...$.*....
            .664.598..
        "}
    }

    fn get_part_two_example_output() -> &'static str {
        "467835"
    }

    fn get_part_two_real_output() -> &'static str {
        "84289137"
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one_example() {
        TestCases::test_part_one_example(true);
    }

    #[test]
    fn test_part_one_real() {
        TestCases::test_part_one_real(false);
    }

    #[test]
    fn test_part_two_example() {
        TestCases::test_part_two_example(true);
    }

    #[test]
    fn test_part_two_real() {
        TestCases::test_part_two_real(false);
    }
}
