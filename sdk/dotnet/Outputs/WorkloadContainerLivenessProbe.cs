// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Cpln.Outputs
{

    [OutputType]
    public sealed class WorkloadContainerLivenessProbe
    {
        public readonly Outputs.WorkloadContainerLivenessProbeExec? Exec;
        public readonly int? FailureThreshold;
        public readonly Outputs.WorkloadContainerLivenessProbeGrpc? Grpc;
        public readonly Outputs.WorkloadContainerLivenessProbeHttpGet? HttpGet;
        public readonly int? InitialDelaySeconds;
        public readonly int? PeriodSeconds;
        public readonly int? SuccessThreshold;
        public readonly Outputs.WorkloadContainerLivenessProbeTcpSocket? TcpSocket;
        public readonly int? TimeoutSeconds;

        [OutputConstructor]
        private WorkloadContainerLivenessProbe(
            Outputs.WorkloadContainerLivenessProbeExec? exec,

            int? failureThreshold,

            Outputs.WorkloadContainerLivenessProbeGrpc? grpc,

            Outputs.WorkloadContainerLivenessProbeHttpGet? httpGet,

            int? initialDelaySeconds,

            int? periodSeconds,

            int? successThreshold,

            Outputs.WorkloadContainerLivenessProbeTcpSocket? tcpSocket,

            int? timeoutSeconds)
        {
            Exec = exec;
            FailureThreshold = failureThreshold;
            Grpc = grpc;
            HttpGet = httpGet;
            InitialDelaySeconds = initialDelaySeconds;
            PeriodSeconds = periodSeconds;
            SuccessThreshold = successThreshold;
            TcpSocket = tcpSocket;
            TimeoutSeconds = timeoutSeconds;
        }
    }
}
