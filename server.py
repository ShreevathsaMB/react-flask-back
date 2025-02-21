from flask import Flask, jsonify

app = Flask(__name__)

comparison_data = {
    "git_comparison": {
        "title": "GitHub vs. GitLab",
        "features": {
            "Repository Management": "Both offer robust repository management.",
            "CI/CD": "GitLab has built-in CI/CD, while GitHub uses GitHub Actions.",
            "Issue Tracking": "Both have strong issue tracking systems.",
            "Pricing": "GitHub has more flexible free tier for public repos. GitLab is strong for private repos.",
        },
    },
    "docker_comparison": {
        "title": "Docker",
        "description": "Docker is a platform for developing, shipping, and running applications in containers.",
        "key_features": ["Containerization", "Image Management", "Docker Compose"],
    },
    "kubernetes_comparison": {
        "title": "Kubernetes",
        "description": "Kubernetes is an open-source container orchestration system.",
        "key_features": ["Automated Deployment", "Scaling", "Service Discovery"],
    },
    "jenkins_comparison": {
        "title": "Jenkins",
        "description": "Jenkins is an open-source automation server.",
        "key_features": ["CI/CD Pipelines", "Plugin Ecosystem", "Extensibility"],
    },
     "flask_react_relationship": {
        "title": "Flask & React: A Dynamic Duo",
        "description": "Flask and React work together to create powerful web applications. Flask serves as the backend, handling data and logic, while React provides a dynamic and interactive frontend.",
        "key_points": [
            "Flask provides API endpoints for React to fetch data.",
            "React renders the UI and handles user interactions.",
            "They communicate via HTTP requests (e.g., GET, POST).",
            "This separation of concerns allows for scalable and maintainable applications.",
        ],
    },
}

@app.route("/comparisons", methods=["GET"])
def get_comparisons():
    return jsonify(comparison_data)

if __name__ == "__main__":
    app.run(debug=True)