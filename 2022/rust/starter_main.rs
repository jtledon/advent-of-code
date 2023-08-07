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

fn part1(data: &String) /* -> u32 */ {
}


fn part2(data: &String) /* -> usize */ {
}
