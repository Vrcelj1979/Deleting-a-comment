#!/usr/bin/env python
import webapp2
from handlers.cron.delete_old_topics import DeleteOldTopicsCron
from crons.delete_comments import DeleteCommentsCron
from handlers.base import CookieAlertHandler, MainHandler
from handlers.comment import CommentAdd, CommentDelete
from handlers.topics import TopicAdd, TopicDetails, TopicDelete
from handlers.workers.email_new_comment import EmailNewCommentWorker


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler, name="main-page"),
    webapp2.Route('/set-cookie', CookieAlertHandler, name="set-cookie"),

    webapp2.Route('/topic/add', TopicAdd, name="topic-add"),

    webapp2.Route('/topic/<topic_id:\d+>', TopicDetails, name="topic-details"),
    webapp2.Route('/topic/<topic_id:\d+>/delete', TopicDelete, name="topic-delete"),

    webapp2.Route('/topic/<topic_id:\d+>/comment/add', CommentAdd, name="comment-add"),
    webapp2.Route('/comment/<comment_id:\d+>/delete', CommentDelete, name="comment-delete"),

    webapp2.Route('/task/email-new-comment', EmailNewCommentWorker, name="task-email-new-comment"),

    webapp2.Route('/cron/delete-old-topics', DeleteOldTopicsCron, name="cron-delete-topics"),
    webapp2.Route("/cron/delete-comments", DeleteCommentsCron, name="cron-delete-comments"),
], debug=True)


