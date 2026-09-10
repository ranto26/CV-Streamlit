import json
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
CONVERT_FORMAT = "%b %Y"

### Tasks info


def get_list(tasks):
    if (tasks == []) or (tasks is None):
        tasks = ""
    else:
        list_of_tasks = [f"- {task}" for task in tasks]
        tasks = "\n".join(list_of_tasks)
    return tasks


def project_info():
    with open("content/projects.json", mode="r", encoding="utf-8") as f:
        projects = json.load(f)
    list_of_text = []
    for projet in projects:
        title = projet.get("title") or "Projet"
        description = projet.get("description") or ""
        tasks = get_list(tasks=projet.get("tasks"))
        project_description = f"### {title}\n\n{description}"
        if len(tasks) != 0:
            project_description = f"{project_description}\n{tasks}"
        list_of_text.append(project_description)
    return "\n\n".join(list_of_text)


### Expérience


def exp_info():
    exp_text = []
    with open("content/experience_pro.json", mode="r", encoding="utf-8") as f:
        experiences = json.load(f)
    for exp in experiences:
        titre = exp.get("titre") or ""
        statut = exp.get("statut") or ""
        entreprise = exp.get("entreprise") or ""
        lieu = exp.get("lieu") or ""
        debut = exp.get("debut") or ""
        fin = exp.get("fin") or ""
        description = exp.get("description")

        ## Convertir les dates
        duree = "######"
        if len(debut) != 0:
            debut = datetime.strptime(debut, DATE_FORMAT).strftime(CONVERT_FORMAT)
            duree = f"{duree} {debut} -"
            if len(fin) != 0:
                fin = datetime.strptime(fin, DATE_FORMAT).strftime(CONVERT_FORMAT)
            else:
                fin = "Actuellement"
            duree = f"{duree} {fin}"

        # Texte
        exp_entete = f"### {titre} - {statut}"
        factory_line = f"#### {entreprise}, {lieu}"
        description = get_list(description)
        the_text = "\n".join([exp_entete, factory_line, duree, description])
        exp_text.append(the_text)

    return "\n\n".join(exp_text)


### Skills


def skill_info():
    with open("content/skills.json", mode="r", encoding="utf-8") as f:
        skills = json.load(f)
    competence_text = []
    for skill in skills:
        title = skill.get("titre")
        content = skill.get("description")
        content = get_list(content)
        skill_text = f"### {title}\n{content}"
        competence_text.append(skill_text)

    return "\n\n".join(competence_text)


### Studies


def school_info():
    with open("content/schools.json", mode="r", encoding="utf-8") as f:
        schools = json.load(f)
    school_text = []

    for study in schools:
        title = study.get("title")
        lieu = study.get("lieu")
        debut = study.get("debut") or ""
        fin = study.get("fin") or ""
        content = get_list(study.get("description"))

        ## Convertir les dates
        duree = "######"
        if len(debut) != 0:
            debut = datetime.strptime(debut, DATE_FORMAT).strftime(CONVERT_FORMAT)
            duree = f"{duree} {debut} -"
            if len(fin) != 0:
                fin = datetime.strptime(fin, DATE_FORMAT).strftime(CONVERT_FORMAT)
            else:
                fin = "Actuellement"
            duree = f"{duree} {fin}"

        ## Texte
        study_head = f"### {title}"
        study_place = f"##### {lieu}"
        the_text = "\n".join([study_head, study_place, duree, content])

        school_text.append(the_text)

    return "\n\n".join(school_text)
