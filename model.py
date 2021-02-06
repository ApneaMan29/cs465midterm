from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/api/activities/<id>', methods=["GET"])
def activity_id(id):
    if ActivityLog.objects.with_id(id) is None:
        abort(404)

    return ActivityLog.objects.with_id(id).dictionary()
