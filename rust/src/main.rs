use solve::Solver;

mod aoc;
mod solve;
mod utils;

#[tokio::main]
async fn main() {
    solve::day_01::solve_part_one().unwrap();
}