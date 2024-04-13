function solve(input) {
    function printPosseStatus(posse) {
        for (const character in posse) {
            console.log(`${character}\n  HP: ${posse[character].hp}\n  Bullets: ${posse[character].bullets}`);
        }
    }

    const assemblePosse = (input) => {
        const n = parseInt(input[0]);
        const posse = {};
        for (let i = 1; i <= n; i++) {
            const [name, hp, bullets] = input[i].split(' ');
            posse[name] = {
                hp: parseInt(hp),
                bullets: parseInt(bullets)
            };
        }

        for (let i = n + 1; i < input.length; i++) {
            const [command, ...params] = input[i].split(' - ');

            switch (command) {
                case 'FireShot':
                    const shooter = posse[params[0]];
                    const target = params[1];
                    if (shooter.bullets > 0) {
                        shooter.bullets--;
                        console.log(`${params[0]} has successfully hit ${target} and now has ${shooter.bullets} bullets!`);
                    } else {
                        console.log(`${params[0]} doesn't have enough bullets to shoot at ${target}!`);
                    }
                    break;

                case 'TakeHit':
                    const victim = posse[params[0]];
                    const damage = parseInt(params[1]);
                    const attacker = params[2];
                    victim.hp -= damage;
                    if (victim.hp > 0) {
                        console.log(`${params[0]} took a hit for ${damage} HP from ${attacker} and now has ${victim.hp} HP!`);
                    } else {
                        delete posse[params[0]];
                        console.log(`${params[0]} was gunned down by ${attacker}!`);
                    }
                    break;

                case 'Reload':
                    const character = posse[params[0]];
                    if (character.bullets < 6) {
                        const bulletsReloaded = Math.min(6 - character.bullets, 6);
                        character.bullets += bulletsReloaded;
                        console.log(`${params[0]} reloaded ${bulletsReloaded} bullets!`);
                    } else {
                        console.log(`${params[0]}'s pistol is fully loaded!`);
                    }
                    break;

                case 'PatchUp':
                    const targetCharacter = posse[params[0]];
                    const recoveryAmount = parseInt(params[1]);
                    targetCharacter.hp = Math.min(targetCharacter.hp + recoveryAmount, 100);
                    if (targetCharacter.hp === 100) {
                        console.log(`${params[0]} is in full health!`);
                    } else {
                        console.log(`${params[0]} patched up and recovered ${recoveryAmount} HP!`);
                    }
                    break;

                case 'Ride Off Into Sunset':
                    return posse;
            }
        }
    };

    const finalPosse = assemblePosse(input);

    printPosseStatus(finalPosse);
}

