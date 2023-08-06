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

fn part1(data: &String) -> u32 {
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

// fn part2(data: &String) -> u32 {
//     for group in 
//     data
//         .split("\n\n")
//         .map(|group| {
//             let lines = group.lines();
//             let sets = lines.map(|rucksack| std::collections::HashSet::from_iter(rucksack.chars()));
//             println!("{sets:?}");
//             let intersect: HashSet<char, _> = 
//                 sets
//                 .reduce(|a: HashSet<char, _>, b: HashSet<char, _>| 
//                         a.intersection(&b)
//                         .cloned()
//                         .collect::<HashSet<char>>())
//                 .unwrap();
//             println!("{intersect:?}");
//             intersect.iter().map(|char| 
//                         match char {
//                             'a'..='z' => (*char as u32) - 'a' as u32 + 1,
//                             'A'..='Z' => (*char as u32) - 'A' as u32 + 26 + 1,
//                             _ => todo!()
//                         })
//             .sum::<u32>()
//         })
//         .sum::<u32>()
// }

fn part2(data: &String) -> u32 {
    let mut res: u32 = 0;
    let group = data.lines().collect::<Vec<&str>>();
    let chunks = group.chunks(3);
    for chunk in chunks {
        let mut sets = vec!();
        for line in chunk {
            let set = std::collections::HashSet::<_>::from_iter(line.chars());
            sets.push(set.clone());
        }
        let intersects = sets
            .iter()
            .skip(1)
            .fold(sets[0].clone(), |acc, hs| {
                acc.intersection(hs).cloned().collect()
            });
        let ints = intersects.iter().map(|char| 
                    match char {
                        'a'..='z' => (*char as u32) - 'a' as u32 + 1,
                        'A'..='Z' => (*char as u32) - 'A' as u32 + 26 + 1,
                        _ => todo!()
                    });
        let int = ints.sum::<u32>();
        res = res + int;
    }
    return res;
}       
