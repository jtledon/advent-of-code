use std::fs;
use std::io;

fn main() {
    let filename: &str = "adventofcode.com_2022_day_1_input.txt";
    let _ = part1(filename);
}


fn part1(filepath: &str) -> () {
    let data: Result<String, io::Error> = fs::read_to_string(filepath);
    let s = match data {
        Ok(s) => s,
        Err(e) => {
            println!("Err({:?}) - {}", e, "entered error case");
            String::from("")}
    };

    let groups = s.split("\n\n");
    let mut agg: Vec<i32> = Vec::new();
    for val in groups {
        let inner_split = val.trim().split("\n");
        let nums = inner_split.map(|num_str| num_str.parse::<i32>().unwrap());
        let sum: i32 = nums.clone().sum();
        // println!("{:?}, final_sum({})", nums, sum);
        agg.push(sum);
        // println!("{:?}", val);
    }
    let max = agg.iter().max();
    println!("{:?}", max)
}
