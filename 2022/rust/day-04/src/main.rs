use std::str::FromStr;

fn main() {
    let data = read_data();
    println!("{:?}", part1(&data));
    println!("{:?}", part2(&data));
}

fn get_file_name() -> String {
    let cwd = std::env::current_dir().ok().unwrap();
    let cwd_str = cwd.to_str().unwrap();

    let re = regex::Regex::new(r"(^.*)/(\d{4})/.*/day-(\d+).*$").unwrap();
    let cap = re.captures(cwd_str).unwrap();
    let leading_dir = cap.get(1).unwrap().as_str();
    let year = cap.get(2).unwrap().as_str();
    let day = cap.get(3).unwrap().as_str().trim_start_matches('0');

    let path = std::path::Path::new(".")
                    .join(leading_dir)
                    .join(year)
                    .join("input-files")
                    .join(format!("adventofcode.com_{year}_day_{day}_input.txt"));
    assert!(path.exists());
    let path_str = path.to_str().unwrap();

    return String::from(path_str);
    
}

fn read_data() -> String {
    let filepath = get_file_name();
    return std::fs::read_to_string(filepath).ok().unwrap();
}

#[derive(Debug, Clone, Copy)]
struct Rng {
    start: u32,
    stop: u32
}

#[derive(Debug, Clone, Copy)]
struct Ranges {
    l: Rng,
    r: Rng
}

struct ParseRangeEror;

impl FromStr for Ranges {
    type Err = ParseRangeEror;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let ranges = s.split(',');
        let nums: Vec<Vec<u32>> = ranges.map(|rng| rng
                                    .split('-')
                                    .map(|num| num.parse::<u32>().unwrap() )
                                    .collect()
                        ).collect();
        let ranges_struct = Ranges {
            l: Rng {
                start: nums[0][0],
                stop: nums[0][1]
            },
            r: Rng {
                start: nums[1][0],
                stop: nums[1][1]
            }
        };
        Ok(ranges_struct)
    }

}

fn full_overlap(first: &Rng, second: &Rng) -> bool {
    first.start <= second.start && first.stop >= second.stop
}

fn part1(data: &String) -> usize {
    let parsed = data
        .lines()
        .map(|line| line.parse::<Ranges>().ok().unwrap())
        .filter(|ranges| full_overlap(&ranges.l, &ranges.r) || full_overlap(&ranges.r, &ranges.l))
        .collect::<Vec<Ranges>>()
        .len();
    return parsed;
}


fn partial_overlap(first: &Rng, second: &Rng) -> bool {
    (second.start..=second.stop).contains(&first.start) ||
    (second.start..=second.stop).contains(&first.stop)
}

fn part2(data: &String) -> usize {
    let parsed = data
        .lines()
        .map(|line| line.parse::<Ranges>().ok().unwrap())
        .filter(|ranges| partial_overlap(&ranges.l, &ranges.r) || partial_overlap(&ranges.r, &ranges.l))
        .collect::<Vec<Ranges>>()
        .len();
    return parsed;
}
