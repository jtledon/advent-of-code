fn main() {
    let data = read_data();
    println!("{:?}", part1(data));
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

fn part1(data: String) -> u32 {
    data
        .lines()
        .map(|line| {
            let half = line.len() / 2;
            let front = &line[..half];
            let back = &line[half..];
            let front_set = std::collections::HashSet::<char>::from_iter(front.chars());
            let back_set = std::collections::HashSet::<char>::from_iter(back.chars());
            let intersect = front_set.intersection(&back_set);
            let ints = intersect.map(|char| 
                    match char {
                        'a'..='z' => (*char as u32) - 'a' as u32 + 1,
                        'A'..='Z' => (*char as u32) - 'A' as u32 + 26 + 1,
                        _ => todo!()
                    });
            // println!("{:?}", ints.clone().sum::<u32>());
            ints.sum::<u32>()
        })
        .sum::<u32>()
}
