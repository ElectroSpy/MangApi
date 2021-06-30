from run import mongo

manga = {
    "titre": "Solo Leveling",
    "auteur": "Sung-Lak Jang",
    "categorie": "Shonen",
    "statut": "En cours",
    "sortie" : "25/08/2019" ,
    "nombre": "155",
    "description": "10 years ago, after “the Gate” that connected the real world with the monster world opened, some of the ordinary, everyday people received the power to hunt monsters within the Gate. They are known as Hunters. However, not all Hunters are powerful. My name is Sung Jin-Woo, an E-rank Hunter. I'm someone who has to risk his life in the lowliest of dungeons, the World's Weakest. Having no skills whatsoever to display, I barely earned the required money by fighting in low-leveled dungeons… at least until I found a hidden dungeon with the hardest difficulty within the D-rank dungeons! In the end, as I was accepting death, I suddenly received a strange power, a quest log that only I could see, a secret to leveling up that only I know about! If I trained in accordance with my quests and hunted monsters, my level would rise. Changing from the weakest Hunter to the strongest S-rank Hunter!",
    "image_card": "https://jolstatic.fr/attachments/8/9/081/6/MzFlZWIwOWViOGEzOGIxZWQ5ZTYzNDAyYWVlODU4N2Q/sololeveling.jpg?quality=90&width=250",
    "image_back": "https://jolstatic.fr/attachments/8/9/081/6/MzFlZWIwOWViOGEzOGIxZWQ5ZTYzNDAyYWVlODU4N2Q/sololeveling.jpg",
},{
    "titre": "The Beginning After The End",
    "auteur": "Turtleme - Fuyuki23",
    "categorie": "Seinen",
    "statut": "En cours",
    "sortie" : "25/08/2019" ,
    "nombre": "31",
    "description": "Reincarnated into a new world filled with magic and monsters, the king has a second chance to relive his life. Correcting the mistakes of his past will not be his only challenge, however. Underneath the peace and prosperity of the new world is an undercurrent threatening to destroy everything he has worked for, questioning his role and reason for being born again.",
    "image_card": "https://mangakik.com/wp-content/uploads/2020/03/33863.jpg?quality=90&width=250",
    "image_back": "https://mangakik.com/wp-content/uploads/2020/03/33863.jpg",
},{
    "titre": "I'm The Great Immortal",
    "auteur": "June Snow Studio",
    "categorie": "Shonen",
    "statut": "En cours",
    "sortie" : "01/04/2018" ,
    "nombre": "1208",
    "description": "The previous life was a peerless genius in the world of immortality. He was killed by 3 celestial beings. He was accidentally reborn to his 20s by the book of heaven. All he wanted to do was to become an immortal and return to the immortal world, and he became the strongest man on the earth, turning his hands into clouds and covering his hands with rain, provoking anyone who defies him! He is the venerable one! The ruler of 3000 worlds! The guy who is 10 000 times better than Thanos! He is Taixuan Taizun! The Great Immortal!",
    "image_card": "https://tse1.mm.bing.net/th?id=OIP.qNzj4CRKx2AmHYgZspW9ZgHaKe&pid=Api.jpg?quality=90&width=250",
    "image_back": "https://tse1.mm.bing.net/th?id=OIP.qNzj4CRKx2AmHYgZspW9ZgHaKe&pid=Api.jpg",
},{
    "titre": "The Second Coming Of Gluttony",
    "auteur": "Ro Yujin - Ahn Jonghyeok",
    "categorie": "Shojo",
    "statut": "En cours",
    "sortie" : "27/12/2019" ,
    "nombre": "67",
    "description": "He was an addict, a loser, a despicable human being. But, one fleeting dream that may not have been a dream at all reawakens his once-lost senses. Possessing a unique ability, he would use that, and the dream, to forge his path in the world now known as the Lost Paradise.",
    "image_card": "https://avt.mkklcdnv6temp.com/7/o/20-1583501314.jpg?quality=90&width=250",
    "image_back": "https://avt.mkklcdnv6temp.com/7/o/20-1583501314.jpg",
},{
    "titre": "The Descent Of The Demonic Master",
    "auteur": "Wolbaek - Mayolang",
    "categorie": "Shonen",
    "statut": "En cours",
    "sortie" : "03/11/2019" ,
    "nombre": "100",
    "description": "The first life. After a tragic accident losing his family and legs, he ends his own life. The second life. He earned fame as the Red Demonic Master in Zhongyuan, but was betrayed by the man he trusted the most. And now comes his third life. In his life back in the modern world, Gang Jinho decides to live a normal life... However, he was too used to the Zhongyuan life to become a normal person! 'I wanted to live peacefully. But you are the ones who started it. I hope you're prepared for this.' In front of the threats of his new life, can Gang Jinho shake off his impulses as the Red Demonic Master and obtain the 'normal life' he desires? The adaptation story of a legendary martial artist in the 21st century!",
    "image_card": "https://www.anime-planet.com/images/manga/covers/the-descent-of-the-demonic-master-42470.jpg?quality=90&width=250",
    "image_back": "https://www.anime-planet.com/images/manga/covers/the-descent-of-the-demonic-master-42470.jpg",
}

mongo.db.mangadb.insert_many(manga)