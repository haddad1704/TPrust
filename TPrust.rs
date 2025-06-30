use std::io;


struct Livre {

  titre:String,
  auteur:String,
  annee:u32,
  dispo:bool,

}




fn ajouter(livres: &mut Vec<Livre>) {

    let mut t = String::new();
    println!("titre  :");
    io::stdin().read_line(&mut t).unwrap();
    let t=t.trim().to_string();

    for l in livres.iter()   {
        if l.titre ==t {
        println!("existe deja ");
        return;
        }
    }

    let mut a=String::new();
    println!("auteur  :");
    io::stdin().read_line(&mut a).unwrap();
    let a=a.trim().to_string();

    let mut an= String::new();
    println!("annee  :");
    io::stdin().read_line(&mut an).unwrap();
    let an:u32 =an.trim().parse().unwrap_or(0);

    livres.push(Livre {
      titre:t,
      auteur:a,
      annee:an,
      dispo:true,
    });

    println!("ajoute");
}


fn afficher(livres:&Vec<Livre>,dispo:bool) {
    for l in livres.iter() {
        if !dispo||l.dispo {
        println!("{}-{}-{}", l.titre,l.auteur,l.annee);
        if l.dispo {
        println!("dispo ");
        } else {
        println!("emprunte ");
        }
        println!("");
        }
    }
}




fn emprunter(livres: &mut Vec<Livre>) {
    let mut nom= String::new();
    println!("titre a emprunter :");
    io::stdin().read_line(&mut nom).ok();
    let nom = nom.trim();
    for l in livres.iter_mut() {
        if l.titre == nom {
        if l.dispo {
        l.dispo = false;
        println!("emprunte ");
        } else {
        println!("deja pris ");
        }
        return;
        }
    }
    println!("pas trouve");
}



fn retour(livres: &mut Vec<Livre>) {
    let mut nom = String::new();
    println!("titre a rendre :");
    io::stdin().read_line(&mut nom).ok();
    let nom = nom.trim();
    for l in livres.iter_mut() {
        if l.titre == nom {
        if !l.dispo {
        l.dispo = true;
        println!("merci ");
        } else {
        println!("non emprunte ");
        }
        return;
        }
    }
    println!("pas trouve");
}



fn main() {
    let mut livres: Vec<Livre> = Vec::new();
    loop {
        println!("1 ajouter");
        println!("2 emprunter");
        println!("3 retour");
        println!("4 afficher tous ");
        println!("5 afficher dispo");
        println!("6 quitter ");
        
        let mut choix = String::new();
        print!("choix : ");
        io::Write::flush(&mut io::stdout()).ok();
        io::stdin().read_line(&mut choix).ok();
        match choix.trim() {
            
            "1" => ajouter(&mut livres),
            "2" => emprunter(&mut livres),
            "3" => retour(&mut livres),
            "4" => afficher(&livres, false),
            "5" => afficher(&livres, true),
            "6" => break,
            _ => println!("choix incorrect"),
        }
    }
}