use solve::index::y2023;

use crate::solve::Solver;

mod aoc;
mod solve;
mod utils;

#[tokio::main]
async fn main() {
    y2023::d02::solve_part_one().unwrap();
    y2023::d02::solve_part_two().unwrap();
}